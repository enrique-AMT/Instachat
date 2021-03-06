import { Component, OnInit, Inject } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { RemoteServerService } from './../bussiness-logic/remote-server.service';
import { NotificationService } from './../bussiness-logic/notifications.service';
import { User } from './../bussiness-logic/User';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA, MatTableDataSource} from '@angular/material';

@Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.css']
})


export class LoginComponent implements OnInit {
    loading = false;
    returnUrl: string;
    public username: string;
    public password: string;

    oldPassword: string;
    newPassword: string;
    confirmNewPassword: string;

    contactList: User[];
  public users: User[] = [];

    constructor(
        private route: ActivatedRoute,
        private router: Router,
        private server: RemoteServerService,
        private notifications: NotificationService,
        public dialog: MatDialog
    ) { }

    // openDialog(): void {
    //     console.log('Before Error');
    //     const dialogRef = this.dialog.open(ResetPasswordComponent, {
    //       width: '300px',
    //       data: {oldPassword: this.oldPassword, newPassword: this.newPassword, confirmNewPassword: this.confirmNewPassword}
    //     });
    //     dialogRef.afterClosed().subscribe(result => {
    //     });
    //   }

    ngOnInit() {
        // get return url from route parameters or default to '/'
        this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
        this.username = '';
        this.password = '';

      localStorage.setItem('first_name','');
      localStorage.setItem('last_name', '');
      localStorage.setItem('user_id', '');
      localStorage.setItem('u_email_address', '');
      localStorage.setItem('phone', '');
      localStorage.setItem('username', '');

      // this.server.getSingleUser('1').subscribe(
      //   data => {
      //     console.log(data);
      //     localStorage.setItem('first_name', data['User']['first_name']);
      //     localStorage.setItem('last_name', data['User']['last_name']);
      //     localStorage.setItem('user_id', data['User']['user_id']);
      //     localStorage.setItem('u_email_address', data['User']['u_email_address']);
      //     localStorage.setItem('phone', data['User']['phone']);
      //     localStorage.setItem('username', data['User']['username']);
      //   },
      //   error => {
      //     console.log(error);
      //     this.notifications.httpError(error);
      //   }
      // );

      // this.server.getUsers().subscribe(
      //   data => {
      //       this.users = data;
      //
      //     this.contactList = data['User'];
      //     console.log(this.contactList);
      //   },
      //   error => {
      //     console.log(error);
      //     if (error.status === 403) {
      //       this.router.navigate(['login']);
      //     }
      //     this.notifications.httpError(error);
      //   }
      // );

    // this.server.getUserContacts('1').subscribe(
    //   data => {
    //     console.log(data);
    //     this.contactList = data['User'];
    //   }
    // );
}

  getUserProfile(username) {
    this.server.getUserProfile(this.username).subscribe(
      data => {
        console.log(data);
        localStorage.setItem('first_name', data['User']['first_name']);
        localStorage.setItem('last_name', data['User']['last_name']);
        localStorage.setItem('user_id', data['User']['user_id']);
        localStorage.setItem('u_email_address', data['User']['u_email_address']);
        localStorage.setItem('phone', data['User']['phone']);
        localStorage.setItem('username', data['User']['username']);

        this.server.getUserContacts(localStorage.getItem('user_id')).subscribe(
          data2 => {
            console.log(data2);
            this.contactList = data2['User'];
            this.router.navigate(['profile']);
          }
        );
      },
      error => {
        console.log(error);
        this.notifications.httpError(error);
      }
    );

  }

  login(username, password) {
    // this.router.navigate(['profile']);
    this.loading = true;

    this.server.login(username, password).subscribe(
      res => {
        this.loading = false;
        console.log('login');
        this.getUserProfile(this.username)
      },
      error => {
        console.log(error);
        this.loading = false;
        this.password = '';
        this.notifications.httpError(error);
      }
    );
  }
  goToChats() {
    this.router.navigate(['chats']);
  }

    showRegister() {
        this.router.navigate(['/register']);
    }

  showAbout() {
    this.router.navigateByUrl('about.html');
  }
}
export interface DialogData {
    oldPassword: string;
    newPassword: string;
    confirmNewPassword: string;
  }
