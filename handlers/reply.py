from flask import jsonify
from daos.reply import ReplyDAO

# rid = 2

# replies_list = [{"reply_id":1,"user_id": "1","post_id": "1", "reply_text": "Hello there", "reply_date": "21-02-2019"}]


class ReplyHandler:

    def build_reply_dict(self, row):
        result = {'reply_id': row[0], 'reply_date': row[1], 'reply_text': row[2]}
        return result

    def build_reply_attributes(self, reply_id, reply_date, reply_text):
        result = {}
        result['reply_id'] = reply_id
        result['reply_date'] = reply_date
        result['reply_text'] = reply_text
        return result

    def getAllReplies(self):
        dao = ReplyDAO()
        reply_list = dao.getAllReplies()
        result_list = []
        for row in reply_list:
          result = self.build_reply_dict(row)
          result_list.append(result)

        return jsonify(Reply=result_list)

    def getReplyById(self, reply_id):
        dao = ReplyDAO()
        return jsonify(Reply=dao.getReplyById(reply_id))

    def getReplyByDate(self, reply_date):
        dao = ReplyDAO()
        return jsonify(Reply=dao.getReplyByDate(reply_date))

    def getReactOnReply(self, reply_id):
        dao = ReplyDAO()
        return jsonify(Reply=dao.getReactsOnReplies(reply_id))


    def createReply(self, json):
        print("TODO")
        # global rid
        # user_id = json['user_id']
        # post_id = json['post_id']
        # reply_text = json['reply_text']
        # reply_date = json['reply_date']
        #
        # if user_id and post_id and reply_text and reply_date:
        #     replies_list.append([{"reply_id": rid, "user_id": user_id, "post_id": post_id,
        #                           "reply_text": reply_text, "reply_date": reply_date}])
        #     result = self.build_reply_attributes(rid, user_id, post_id, reply_text, reply_date)
        #     rid = (rid + 1)
        #     return jsonify(Reply=result), 201
        # else:
        #     return jsonify(Error="Unexpected attributes in post request"), 400

    def updateReply(self, reply_id, json):
        print("TODO")
        # if len(replies_list) < reply_id or reply_id < 1:
        #     return jsonify(Error = "Reply not found."), 404
        # else:
        #     if len(json) != 5:
        #         return jsonify(Error = "Update request incorrect."), 400
        #     else:
        #         user_id = json['user_id']
        #         post_id = json['post_id']
        #         reply_text = json['reply_text']
        #         reply_date = json['reply_date']
        #
        #         if user_id and post_id and reply_text and reply_date:
        #             return jsonify(UpdateStatus = "AREA TO UPDATE REPLY BY ID"), 200

    def deleteReply(self, reply_id):
        print("TODO")
        # global p_id
        # if len(replies_list) < reply_id or reply_id < 1:
        #     return jsonify(Error = "Session not found."), 404
        # else:
        #     return jsonify(DeleteStatus = "AREA TO DELETE REPLY BY ID"), 200
