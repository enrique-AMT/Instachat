import { Component, OnInit, Inject } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { RemoteServerService } from './../bussiness-logic/remote-server.service';
import {DataSource} from '@angular/cdk/collections';
import { NotificationService } from './../bussiness-logic/notifications.service';
import { User } from './../bussiness-logic/User';
import { Observable } from 'rxjs/Observable';
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA, MatTableDataSource} from '@angular/material';

export interface DashboardPost {
  post_date: string;
  post_count: number;
}

export class DashboardHashtag {
  constructor(
    public hash_name: string,
    public hashtag_id: number,
    public position: number

  ) { }
}

export class DashboardLike {
  constructor(
    public react_date: string,
    public react_type: string,
    public react_count: number

  ) { }
}

export class DashboardDislike {
  constructor(
    public react_date: string,
    public react_type: string,
    public react_count: number

  ) { }
}

export class DashboardUser {
  constructor(
    public post_date: string,
    public username: string,
    public post_count: number

  ) { }
}

export class DashboardUserPost {
  constructor(
    public post_date: string,
    public post_count: number
  ) { }
}

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {

  dataSource = new DashboardPostDataSource(this.server);
  hashtagSource: DashboardHashtagDataSource;
  likesSource: DashboardLikeDataSource;
  dislikeSource: DashboardDislikeDataSource;
  userSource: DashboardUserDataSource;
  userPost: DashboardUserPostDataSource;

  endedFetch = false;
  hashtagsResults: any[];
  likesResults: any[];
  dislikesResults: any[];
  userResults: any[];
  userPostResults: any[];


  public hashtagList =  Array<DashboardHashtagDataSource>();
  public likesList =  Array<DashboardLikeDataSource>();
  public dislikesList =  Array<DashboardDislikeDataSource>();
  public userList =  Array<DashboardUserDataSource>();
  public userPostList =  Array<DashboardUserPostDataSource>();


  hashtagsColumns = ['hash_name', 'position'];
  displayedColumns = ['date', 'posts'];
  likesColumns = ['react_date', 'react_count'];
  dislikesColumns = ['react_date', 'react_count'];
  userColumns = ['post_date', 'username', 'post_count'];
  userPostColumns = ['post_date', 'post_count'];

  results: any[];
  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private server: RemoteServerService,
    private notifications: NotificationService,
    public dialog: MatDialog
  ) { }

  ngOnInit() {

    if (localStorage.getItem('user_id') === '' || localStorage.getItem('user_id') === null) {
      this.router.navigate(['login']);
    }

    this.server.getDashboardPosts().subscribe(
      data => {


         this.dataSource = data['Post'];
       // console.log(this.dataSource);

        this.results = data['Post'];
         console.log(this.results);
        // this.results.forEach(item => {


          /////////////////// Hashtags ///////////////////////////
          this.server.getTrendingHashtags().subscribe(
            data2 => {
               console.log(data2);
              this.hashtagsResults = data2['Hashtag'];
              this.hashtagsResults.forEach(item2 => {
                console.log(item2);
                this.hashtagList.push(item2);
              });

             // this.endedFetch = true;
              console.log(this.hashtagList);
            });
          // until here
        // });
        /////////////////// Hashtags ///////////////////////////

        /////////////////// Likes ///////////////////////////
        this.server.getDashboardLikes().subscribe(
          data3 => {
            console.log('Likes');
             console.log(data3);
            this.likesResults = data3['Reacts'];
            this.likesResults.forEach(item3 => {
              console.log(item3);
              this.likesList.push(item3);
            });

           //  this.endedFetch = true;
            console.log(this.likesList);
          });
        /////////////////// Likes ///////////////////////////

        /////////////////// Dislikes ///////////////////////////
        this.server.getDashboardDislikes().subscribe(
          data4 => {
            console.log('Dislikes');
            console.log(data4);
            this.likesResults = data4['Reacts'];
            this.likesResults.forEach(item4 => {
              console.log(item4);
              this.dislikesList.push(item4);
            });

         //   this.endedFetch = true;
            console.log(this.dislikesList);
          });
        /////////////////// Dislikes ///////////////////////////

        /////////////////// Users ///////////////////////////
        this.server.getDashboardUsers().subscribe(
          data5 => {
            console.log('Users');
            console.log(data5);
            this.userResults = data5['User'];
            this.userResults.forEach(item5 => {
              console.log(item5);
              this.userList.push(item5);
            });

            // this.endedFetch = true;
            console.log(this.userList);
          });
        /////////////////// Users ///////////////////////////

        /////////////////// User Posts ///////////////////////////
        this.server.getDashboardUserPosts(localStorage.getItem('user_id')).subscribe(
          data6 => {
            console.log('User Posts');
            console.log(data6);
            this.userPostResults = data6['Post'];
            this.userPostResults.forEach(item6 => {
              console.log(item6);
              this.userPostList.push(item6);
            });

            this.endedFetch = true;
            console.log(this.userPostList);
          });
        /////////////////// User Posts ///////////////////////////

      },
      error => {
        console.log(error);
        this.notifications.httpError(error);
      }
    );
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
export class DashboardPostDataSource extends DataSource<any> {
  constructor(private dashboardService: RemoteServerService) {
    super();
  }
  connect(): Observable<DashboardPost[]> {
    return this.dashboardService.getDashboardPosts();
  }
  disconnect() {}
}

export class DashboardHashtagDataSource extends DataSource<any> {
  constructor(private dashboardService: RemoteServerService) {
    super();
  }
  connect(): Observable<DashboardHashtag[]> {
    const data = this.dashboardService.getTrendingHashtags();
    return data;
  }
  disconnect() {}
}

export class DashboardLikeDataSource extends DataSource<any> {
  constructor(private dashboardService: RemoteServerService) {
    super();
  }
  connect(): Observable<DashboardLike[]> {
    return this.dashboardService.getDashboardLikes();
  }
  disconnect() {}
}

export class DashboardDislikeDataSource extends DataSource<any> {
  constructor(private dashboardService: RemoteServerService) {
    super();
  }
  connect(): Observable<DashboardDislike[]> {
    return this.dashboardService.getDashboardDislikes();
  }
  disconnect() {}
}

export class DashboardUserDataSource extends DataSource<any> {
  constructor(private dashboardService: RemoteServerService) {
    super();
  }
  connect(): Observable<DashboardUser[]> {
    return this.dashboardService.getDashboardUsers();
  }
  disconnect() {}
}

export class DashboardUserPostDataSource extends DataSource<any> {
  constructor(private dashboardService: RemoteServerService) {
    super();
  }
  connect(): Observable<DashboardUserPost[]> {
    return this.dashboardService.getDashboardUserPosts(localStorage.getItem('user_id'));
  }
  disconnect() {}
}


