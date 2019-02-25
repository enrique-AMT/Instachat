from flask import jsonify

rid = 1


class ReplyHandler:

    def build_reply_dict(self, row):
        reply_list = {'reply_id': row[0], 'user_id': row[1], 'post_id': row[2], 'reply_text': row[3],
                      'reply_date': row[4]}
        return reply_list

    def build_reply_attributes(self, reply_id, user_id, post_id, reply_text, reply_date):
        result = {}
        result['reply_id'] = reply_id
        result['user_id'] = user_id
        result['post_id'] = post_id
        result['reply_text'] = reply_text
        result['reply_date'] = reply_date

        return result

    def getAllReplies(self):
        reply_list = [['1', '1', '1', 'Hello there', '21-02-2019']]
        result_list = []
        for row in reply_list:
            result = self.build_reply_dict(row)
            result_list.append(result)
        return jsonify(Reply=result_list)

    def createReply(self, json):
        global rid
        replies_list = [['1', '1', '1', '1', 'Hello there', '21-02-2019']]
        reply_id = json['reply_id']
        user_id = json['user_id']
        post_id = json['post_id']
        reply_text = json['reply_text']
        reply_date = json['reply_date']

        if reply_id and user_id and post_id and reply_text and reply_date and reply_date:
            reply_id = (rid + 1)
            replies_list.append([reply_id, user_id, post_id, reply_text, reply_date])
            result = self.build_reply_attributes(reply_id, user_id, post_id, reply_text, reply_date)
            return jsonify(Part=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
