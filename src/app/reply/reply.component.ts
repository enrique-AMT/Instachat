import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {RemoteServerService} from '../bussiness-logic/remote-server.service';
import {NotificationService} from '../bussiness-logic/notifications.service';
import {MatDialog} from '@angular/material';
import {Chats} from '../bussiness-logic/Chats';
import {Posts} from '../bussiness-logic/Posts';
import {Reply} from '../bussiness-logic/Reply';

@Component({
  selector: 'app-reply',
  templateUrl: './reply.component.html',
  styleUrls: ['./reply.component.scss']
})
export class ReplyComponent implements OnInit {

  id: string;
  public chat: Chats;
  public post: Posts;
  public chat_id: string;
  public post_id: string;
  public reply_text: string;
  replyList: Reply[];


  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private server: RemoteServerService,
    private notifications: NotificationService,
    public dialog: MatDialog
  ) { }

  ngOnInit() {

    this.reply_text = '';

    this.route.params.subscribe(params => {
      this.chat_id = params['id'];
      this.post_id = params['post_id'];
      console.log((this.chat_id));
    });

    this.server.getChatById(this.chat_id).subscribe(
      data => {
        console.log(data['Chat']);
        this.chat = data['Chat'];

      });


    this.server.getPostInChat(this.chat_id, this.post_id).subscribe(
      data => {
        console.log(data);
        this.post = data['Post'];

        this.server.getSingleUser(this.post.p_created_by).subscribe(
          data2 => {
            console.log(data2['User']);
            const user = data2['User'];
            this.post.username = user['first_name'] + ' ' + user['last_name'];

          },
          error => {
            console.log(error);
            this.notifications.httpError(error);
          }
        );
      });

    this.server.getRepliesInPost(this.post.post_id).subscribe(
      data => {
        console.log(data);

      },
      error => {
        console.log(error);
        this.notifications.httpError(error);
      }
    );
  }

  createReply() {
    this.reply_text = (<HTMLInputElement>document.getElementById('reply_text')).value;

    this.server.createReply(this.reply_text, this.post_id, localStorage.getItem('user_id')).subscribe(
      data => {
        console.log(data);
         window.location.reload();

      },
      error => {
        console.log(error);
        this.notifications.httpError(error);
      }
    );
  }

  goToChats() {
    this.router.navigate(['chatsList']);
  }
  goToProfile() {
    this.router.navigate(['profile']);
  }
  goToDashboard() {
    this.router.navigate(['dashboard']);
  }

  backToChat() {
    this.router.navigate(['chatsList/chat/', this.chat_id]);
  }

}
