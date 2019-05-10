import { Component, OnInit, Inject } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { RemoteServerService } from './../bussiness-logic/remote-server.service';
import { NotificationService } from './../bussiness-logic/notifications.service';
import { User } from './../bussiness-logic/User';
import {Chats} from '../bussiness-logic/Chats';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA, MatTableDataSource} from '@angular/material';
import {UserContactsDataSource} from '../profile/profile.component';

@Component({
  selector: 'app-create-chat',
  templateUrl: './create-chat.component.html',
  styleUrls: ['./create-chat.component.scss']
})
export class CreateChatComponent implements OnInit {

  dataSource: UserContactsDataSource;
  displayedColumns = ['Name'];
  selectedUsers: number[] = [];
  isEnabled = false;
  chatName = '';



  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private server: RemoteServerService,
    private notifications: NotificationService,
    public dialog: MatDialog
  ) { }

  ngOnInit() {

    this.server.getUserContacts(localStorage.getItem('user_id')).subscribe(
      data => {
        console.log(data);

        this.dataSource = new UserContactsDataSource(this.server);
        this.dataSource = data['Contact'];
        // this.contactList = data['User'];
      }
    );
  }

  onSelection(e, v) {

    let isSelected = false;
    console.log(this.selectedUsers);

    for (let i = 0; i < this.selectedUsers.length; i++) {
      if ( this.selectedUsers[i] === e['option'].value.user_id) {
        this.selectedUsers.splice(i, 1);
        console.log('After Removing');
        console.log(this.selectedUsers);
        isSelected = true;

        if (this.selectedUsers.length === 0) {
          this.isEnabled = false;
        }
      }
    }
      if (!isSelected) {
        console.log('After Adding');
        this.selectedUsers.push(e['option'].value.user_id);
        this.isEnabled = true;
        console.log(this.selectedUsers);
      }
  }

  createChat() {
    console.log(this.chatName);
    if (this.chatName !== '') {
      this.server.createChat(this.chatName, localStorage.getItem('user_id')).subscribe(
        data => {
        //  console.log('Response: ');
        //  console.log(data['Chat']['chat_id']);

         const chat_id = data['Chat']['chat_id'];
         let added = 0;

          for (let i = 0; i < this.selectedUsers.length; i++) {
            if (this.selectedUsers[i] !== null) {
              console.log(this.selectedUsers[i]);

              this.server.addParticipantToChat(chat_id, this.selectedUsers[i].toLocaleString()).subscribe(
                data2 => {
                  added ++;
                  console.log(data);
                  console.log('Adding Participant');

                  if (added === this.selectedUsers.length) {
                    // go to chat screen
                    console.log('Added All Participants');
                    this.router.navigate(['chatsList/chat/' + chat_id]);
                  }
                });
            }
          }

        });
    } else {
      console.log('Invalid Name');
    }
  }

  goToProfile() {
    this.router.navigate(['profile']);
  }
  goToDashboard() {
    this.router.navigate(['dashboard']);
  }
  goToChats() {
    this.router.navigate(['chatsList']);
  }

}
