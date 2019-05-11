export class Reply {
  constructor(
    public reply_id: string,
    public reply_text: string,
    public p_replied: string,
    public user_that_replied: string,
    public reply_date: string,
    public username: string
  ) { }

  static fromJSON(json: Object): Reply {
    return new Reply(
      json['reply_id'],
      json['reply_text'],
      json['p_replied'],
      json['user_that_replied'],
      json['reply_date'],
      ''
    );
  }

  static fromList(list: Object[]): Reply[] {
    const rep: Reply[] = [];
    list.map( item => {
      rep.push(Reply.fromJSON(item));
    });
    return rep;
  }
}

