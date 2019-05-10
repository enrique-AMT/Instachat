import { Injectable } from '@angular/core';
import {
  HttpClient,
  HttpHeaders,
  HttpErrorResponse,
  HttpParams
} from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';
import { map, catchError } from 'rxjs/operators';
import { User } from './User';
import {Posts} from './Posts';
import {DashboardPost} from '../dashboard/dashboard.component';
import {DashboardHashtag} from '../dashboard/dashboard.component';
import {Chats} from './Chats';

@Injectable()
export class RemoteServerService {
  constructor(private http: HttpClient) { }
  private loggedIn = false;

  private head = new HttpHeaders({
    'Content-type': 'application/json',
    'Access-Control-Allow-Methods': 'POST,GET,OPTIONS,PUT,DELETE',
    'Access-Control-Allow-Origin': 'http://localhost:4200',
    'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept, token'
  });

  private getModifiedHeader() {
    return {
      headers: this.head.append('Authorization', localStorage.getItem('token'))
    };
  }

  public isLoggedIn(): boolean {
    return this.loggedIn;
  }

  public getHome(): Observable<Object> {
    return this.http.get(
      'http://localhost:5000/InstaChat/home/',
      this.getModifiedHeader()
    );
  }

  public getUsers(): Observable<User[]> {
    return this.http
      .get<User[]>(
        'http://localhost:5000/InstaChat/users'
      );
  }

  public getSingleUser(id: string): Observable<User> {
    return this.http
      .get<User>(
        'http://localhost:5000/InstaChat/users/' + id );
  }

  public getUserProfile(username: string): Observable<User> {
    return this.http.get<User>('http://localhost:5000/InstaChat/users/' + username);
  }


  public getUserContacts(id: string): Observable<User[]> {
    return this.http
      .get<User[]>(
        'http://localhost:5000/InstaChat/users/' + id + '/contacts');
  }



  public getDashboardPosts(): Observable<DashboardPost[]> {
    return this.http
      .get<DashboardPost[]>(
        'http://localhost:5000/InstaChat/dashboard/posts'
      );
  }

  public getAllChats(): Observable<Chats[]> {
    return this.http.get<Chats[]>('http://localhost:5000/InstaChat/chats');
  }

  public getChatById(id: string): Observable<Chats> {
    return this.http.get<Chats>('http://localhost:5000/InstaChat/chats/' + id );
  }

  public getChatPosts(id: string): Observable<Posts> {
    return this.http.get<Posts>('http://localhost:5000/InstaChat/chats/' + id + '/posts' );
  }

  public getChatUsers(id: string): Observable<User[]> {
    return this.http.get<User[]>('http://localhost:5000/InstaChat/chats/' + id + '/users' );
  }

  public getPostsReactions(post_id: string, react_type: string): Observable<Posts> {
    return this.http.get<Posts>('http://localhost:5000/InstaChat/posts/' + post_id + '/reacts/' + react_type );
  }

  public getPostUserReactions(post_id: string, react_type: string): Observable<User[]> {
    return this.http.get<User[]>('http://localhost:5000/InstaChat/users/posts/' + post_id + '/' + react_type );
  }


  public getTrendingHashtags(date: string): Observable<DashboardHashtag[]> {
    return this.http
      .get<DashboardHashtag[]>(
        'http://localhost:5000/InstaChat/dashboard/' + date + '/hashtags'
      );
  }


  public login(username: string, password: string) {
    const body = {
      username: username,
      password: password
    };
    return this.http
      .post('http://localhost:5000/InstaChat/login', body);
  }

  public register(
    email: string,
    password: string,
    username: string,
    firstName: string,
    lastName: string
  ) {
    const body = {
      u_email_address: email,
      u_password: password,
      username: username,
      first_name: firstName,
      last_name: lastName
    };
    return this.http
      .post(
        'http://localhost:5000/InstaChat/users',
        body
      )
      .pipe(
        map(res => {
          this.loggedIn = true;
        })
      );
  }

  public removeChat(chat_id: string, owner_id: string) {
    return this.http.delete('http://localhost:5000/InstaChat/chats/' + chat_id + '/owner/' + owner_id);
  }

   public createChat(name: string, owner: string) {
     const body = {
       chat_name: name,
       owner_id: owner
     };
     return this.http
       .post(
         'http://localhost:5000/InstaChat/chats',
         body
       );
   }

   public createPost(chat_id: string, owner_id: string, user_id: string, text: string) {
     const body = {
       post_caption: text,
       p_created_by: user_id,
       c_post_belongs: chat_id
     };
     return this.http
       .post(
         'http://localhost:5000/InstaChat/posts',
         body
       );
   }

   public reactPost(type: string , user_id, post_id) {
     const body = {
       react_type: type,
       user_that_react: user_id,
       p_reacted: post_id

     };
     return this.http
       .post(
         'http://localhost:5000/InstaChat/reacts',
         body
       );
   }

   public addParticipantToChat(chat_id: string, user_id: string) {
     const body = {
       chat_id: chat_id,
       user_id: user_id
     };
     return this.http
       .post(
         'http://localhost:5000/InstaChat/chats/' + chat_id + '/users/' + user_id,
         body
       );
   }

  private handleError(error: HttpErrorResponse) {
    console.error('server error:', error);
    if (error.error instanceof Error) {
      const errMessage = error.error.message;
      return Observable.throw(errMessage);
      // Use the following instead if using lite-server
      // return Observable.throw(err.text() || 'backend server error');
    }
    return Observable.throw(error || 'Node.js server error');
  }

  public postFile(data: FormData) {
    const params = new HttpParams();

    const options = {
      headers: new HttpHeaders().set('Authorization', localStorage.getItem('token')),
      params: params,
      reportProgress: true,
    };

    return this.http.post(
      '',
      data, options
    );
  }

}
