import { Component, OnInit, Inject } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { RemoteServerService } from './../bussiness-logic/remote-server.service';
import { NotificationService } from './../bussiness-logic/notifications.service';
import { User } from './../bussiness-logic/User';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA, MatTableDataSource} from '@angular/material';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  public email: string;
  public password: string;
  public firstName: string;
  public lastName: string;
  public username: string;
  public phone: string;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private server: RemoteServerService,
    private notifications: NotificationService,
    public dialog: MatDialog
  ) { }

  ngOnInit() {
    this.email = '';
    this.password = '';
    this.username = '';
    this.firstName = '';
    this.lastName = '';
    this.phone = '';

  //   this.server.addPhone('16', '7877777777').subscribe(
  //     data2 => {
  //       console.log('added phone');
  //       console.log(data2);
  //
  //
  //       // localStorage.setItem('phone', data['User']['phone']);
  //       // this.router.navigate(['profile']);
  //     },
  //   error => {
  //     console.log(error);
  //     this.notifications.httpError(error);
  //   }
  // );

  }

  createAccount() {
    console.log('Creating Account');
    console.log(this.email);
    console.log(this.password);
    console.log(this.username);
    console.log(this.firstName);
    console.log(this.lastName);
    console.log(this.phone);

    this.server.register(this.email, this.password, this.username, this.firstName, this.lastName).subscribe(
      res => {
       // this.loading = false;
        console.log('Account Created');
        console.log(res);

        this.server.getUserProfile(this.username).subscribe(
          data => {
            console.log('Profile');
            console.log(data);
            this.server.addPhone(data['User']['user_id'], this.phone).subscribe(
              data2 => {
                console.log('added phone');
                console.log(data2);


                localStorage.setItem('phone', this.phone);
                this.router.navigate(['profile']);
              })

           // console.log(data);
            localStorage.setItem('first_name', data['User']['first_name']);
            localStorage.setItem('last_name', data['User']['last_name']);
            localStorage.setItem('user_id', data['User']['user_id']);
            localStorage.setItem('u_email_address', data['User']['u_email_address']);
            localStorage.setItem('username', data['User']['username']);

            // this.router.navigate(['profile']);

          },
          error => {
            console.log(error);
            this.notifications.httpError(error);
          }
        );
      },
      error => {
        console.log('Error');

        this.notifications.httpError(error);
      }
    );  }

  back() {
    this.router.navigate(['/login']);
  }


}
