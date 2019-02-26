from flask import jsonify

rid = 2

replies_list = [[1, '1', '1', 'Hello there', '21-02-2019']]

class ReplyHandler:

    def build_reply_dict(self, row):
        result = {'reply_id': row[0], 'user_id': row[1], 'post_id': row[2], 'reply_text': row[3],
                      'reply_date': row[4]}
        return result

    def build_reply_attributes(self, reply_id, user_id, post_id, reply_text, reply_date):
        result = {}
        result['reply_id'] = reply_id
        result['user_id'] = user_id
        result['post_id'] = post_id
        result['reply_text'] = reply_text
        result['reply_date'] = reply_date

        return result

    def getAllReplies(self):
        result_list = []
        for row in replies_list:
            result = self.build_reply_dict(row)
            result_list.append(result)
        return jsonify(Reply=result_list)

    def getReplyById(self, reply_id):
        if len(replies_list) < reply_id or reply_id < 1:
            return jsonify(Error='User not found'), 404
        else:
            return jsonify(Reply=replies_list[reply_id-1])

    def createReply(self, json):
        global rid
        user_id = json['user_id']
        post_id = json['post_id']
        reply_text = json['reply_text']
        reply_date = json['reply_date']

        if user_id and post_id and reply_text and reply_date:
            replies_list.append([rid, user_id, post_id, reply_text, reply_date])
            result = self.build_reply_attributes(rid, user_id, post_id, reply_text, reply_date)
            rid = (rid + 1)
            return jsonify(Reply=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateReply(self, reply_id, json):
        if len(replies_list) < reply_id or reply_id < 1:
            return jsonify(Error = "Reply not found."), 404
        else:
            if len(json) != 5:
                return jsonify(Error = "Update request incorrect."), 400
            else:
                user_id = json['user_id']
                post_id = json['post_id']
                reply_text = json['reply_text']
                reply_date = json['reply_date']

                if user_id and post_id and reply_text and reply_date:
                    return jsonify(UpdateStatus = "AREA TO UPDATE REPLY BY ID"), 200

    def deleteReply(self, reply_id):
        global p_id
        if len(replies_list) < reply_id or reply_id < 1:
            return jsonify(Error = "Session not found."), 404
        else:
            return jsonify(DeleteStatus = "AREA TO DELETE REPLY BY ID"), 200