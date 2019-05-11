import { Component, OnInit, Inject } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { RemoteServerService } from './../bussiness-logic/remote-server.service';
import { NotificationService } from './../bussiness-logic/notifications.service';
import { User } from './../bussiness-logic/User';
import {Chats} from '../bussiness-logic/Chats';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA, MatTableDataSource} from '@angular/material';
import {printLine} from 'tslint/lib/verify/lines';



export interface DialogData {
  chat_name: string;
  owner_id: string;
}
@Component({
  selector: 'app-chats',
  templateUrl: './chatsList.component.html',
  styleUrls: ['./chatsList.component.scss']
})

export class ChatsListComponent implements OnInit {

  chatlist: Chats[];
  chat_name: string;
  owner_id: string;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private server: RemoteServerService,
    private notifications: NotificationService,
    public dialog: MatDialog
  ) {}

  ngOnInit() {

    if (localStorage.getItem('user_id') === '' || localStorage.getItem('user_id') === null) {
      this.router.navigate(['login']);
    }

    this.server.getUserChatList(localStorage.getItem('user_id')).subscribe(
      data => {
      //  console.log(data);
        this.chatlist = data['Chat'];
        console.log(this.chatlist);
  });
  }

  goToChats(id: string) {
    console.log(id);
    this.router.navigate(['chatsList']);
  }
  goToChat(id: string) {
    console.log(id);
    this.router.navigate(['chatsList/chat/', id ]);
  }
  goToProfile() {
    this.router.navigate(['profile']);
  }
  goToDashboard() {
    this.router.navigate(['dashboard']);
  }

  removeChat(chat_id: string, owner_id: string) {
    this.server.removeChat(chat_id, owner_id).subscribe(
      refresh => {
        console.log('Chat deleted')
        this.router.navigate(['chatsList']);
      },
      error => {
        console.log(error)
        this.notifications.httpError(error);
      }
    );
  }

  createChat() {
    this.router.navigate(['createChat']);
  }
  //   const dialogRef = this.dialog.open(CreateChatDialogComponent, {
  //     width: '400px',
  //     data: {chat_name: this.chat_name, owner_id: this.owner_id}
  //   });
  //   dialogRef.afterClosed().subscribe(result => {
  //     console.log('The dialog was closed');
  //     this.chat_name = result;
  //     this.owner_id = '1';
  //   });
  //
  //   this.server.createChat(this.chat_name, this.owner_id).subscribe(
  //     refresh => {
  //       console.log('Chat created')
  //       this.router.navigate(['chatslist']);
  //     },
  //     error => {
  //       console.log(error)
  //       this.notifications.httpError(error);
  //     }
  //   );
  // }
}


@Component({
  selector: 'app-create-chat-dialog',
  templateUrl: 'createChat-dialog.component.html',
})
export class CreateChatDialogComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<CreateChatDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData) {}

  ngOnInit() {

}

  onNoClick(): void {
    this.dialogRef.close();
  }

}
