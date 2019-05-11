import {Component, Inject, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {RemoteServerService} from '../bussiness-logic/remote-server.service';
import {NotificationService} from '../bussiness-logic/notifications.service';
import {MAT_DIALOG_DATA, MatDialog, MatDialogRef} from '@angular/material';
import {Chats} from '../bussiness-logic/Chats';
import {DashboardPost, DashboardPostDataSource} from '../dashboard/dashboard.component';
import {DataSource} from '@angular/cdk/table';
import {Observable} from 'rxjs/Observable';
import {User} from '../bussiness-logic/User';
import {DialogData} from '../chatsList/chatsList.component';
import {UserContactsDataSource} from '../profile/profile.component';



@Component({
  selector: 'app-chat-info',
  templateUrl: './chat-info.component.html',
  styleUrls: ['./chat-info.component.scss']
})




export class ChatInfoComponent implements OnInit {


  id: string;
  chat: Chats;
  owner: User;

 //  participantsDataSource: UserContactsDataSource;
  dataSource: MembersDataSource;
  displayedColumns = ['name', 'user_id'];
  selectedUsers: number[] = [];
  isEnabled = false;


  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private server: RemoteServerService,
    private notifications: NotificationService,
    public dialog: MatDialog
  ) {
  }

  ngOnInit() {

    if (localStorage.getItem('user_id') === '' || localStorage.getItem('user_id') === null) {
      this.router.navigate(['login']);
    }

    this.route.params.subscribe(params => {
      this.id = params['id'];
    });
    console.log(this.id);

    this.server.getChatById(this.id).subscribe(
      data => {
        console.log(data['Chat']);
        this.chat = data['Chat'];

        this.server.getChatUsers(this.chat.chat_id).subscribe(
          data2 => {
            console.log(data2);
            this.dataSource = new MembersDataSource(this.server, this.chat);
            this.dataSource = data2['Chat'];
          },
          error => {
            console.log(error);
            this.notifications.httpError(error);
          }
        );

        this.server.getSingleUser('1').subscribe(
          data2 => {
            console.log(data2);
            this.owner = data2['User'];
          },
          error => {
            console.log(error);
            this.notifications.httpError(error);
          }
        );
      });
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

  addParticipant() {
      const dialogRef = this.dialog.open(AddParticipantDialogComponent, {
        width: '400px',
        data: {chat: this.chat}
      });
      dialogRef.afterClosed().subscribe(result => {
        console.log('The dialog was closed');
      });

  }

  backToChat() {
    this.router.navigate(['chatsList/chat/', this.chat.chat_id]);
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
}
export class MembersDataSource extends DataSource<any> {
  constructor(private membersService: RemoteServerService, private chat: Chats) {
    super();
  }
  connect(): Observable<User[]> {
    return this.membersService.getChatUsers(this.chat.chat_id);
  }
  disconnect() {}
}


@Component({
  selector: 'app-add-participant-dialog',
  templateUrl: 'addParticipant-dialog.component.html',
  styleUrls: ['./addParticipant-dialog.component.scss']
})
export class AddParticipantDialogComponent implements OnInit {

  participantsDataSource: UserContactsDataSource;
  selectedUsers: number[] = [];
  isEnabled = false;
  chat: Chats;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private server: RemoteServerService,
    private notifications: NotificationService,
    public dialog: MatDialog,
    public dialogRef: MatDialogRef<AddParticipantDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: DialogData) {

    console.log(data);
    this.chat = data['chat'];
  }

  ngOnInit() {
    this.server.getUserContacts(localStorage.getItem('user_id')).subscribe(
      data => {
        console.log(data);
        this.participantsDataSource = new UserContactsDataSource(this.server);
        this.participantsDataSource = data['Contact'];
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

  addParticipants() {

    for (let i = 0; i < this.selectedUsers.length; i++) {
      if (this.selectedUsers[i] !== null) {
        console.log(this.selectedUsers[i]);

        let added = 0;

        this.server.addParticipantToChat(this.chat.chat_id, this.selectedUsers[i].toLocaleString()).subscribe(
          data => {
            added ++;
            console.log(data);
            console.log('Adding Participant');

            if (added === this.selectedUsers.length) {
              // go to chat screen
              console.log('Added All Participants');
              this.dialogRef.close();
              window.location.reload();
            }
          },
          error => {
            console.log(error);
            this.notifications.error('Participant already in chat');
          });
      }
    }
  }

  onNoClick(): void {
    this.dialogRef.close();
  }
}

