from flask import jsonify
from daos.reply import ReplyDAO
from daos.posts import PostsDAO
from daos.users import UsersDAO

# rid = 2

# replies_list = [{"reply_id":1,"user_id": "1","post_id": "1", "reply_text": "Hello there", "reply_date": "21-02-2019"}]


class ReplyHandler:

    def build_reply_dict(self, row):
        result = {'reply_id': row[0],  'reply_text': row[1], 'p_replied': row[2],
                  'user_that_replied': row[3], 'reply_date': row[4]}
        return result

    def build_reply_attributes(self, reply_text, p_replied, user_that_replied):
        result = {}
        result['reply_text'] = reply_text
        result['p_replied'] = p_replied
        result['user_that_replied'] = user_that_replied
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
        row = dao.getReplyById(reply_id)
        if not row:
            return jsonify(Error="Reply Not Found"), 404
        else:
            reply = self.build_reply_dict(row)
            return jsonify(Reply=reply)

    def getReplyByDate(self, reply_date):
        dao = ReplyDAO()
        return jsonify(Reply=dao.getReplyByDate(reply_date))

    def getReactOnReply(self, reply_id):
        dao = ReplyDAO()
        return jsonify(Reply=dao.getReactsOnReply(reply_id))

    def getPostReplies(self, post_id):
        dao = ReplyDAO()
        replies = dao.getPostReplies(post_id)
        reply_list = []
        for row in replies:
            reply_list.append(self.build_reply_dict(row))
        return jsonify(Reply=reply_list)

    def insertReply(self, json):
        # reply_date = json['reply_date']
        reply_text = json['reply_text']
        p_replied = json['p_replied']
        user_that_replied = json['user_that_replied']
        post = PostsDAO().getPostById(p_replied)
        user = UsersDAO().getUserById(user_that_replied)
        if not post:
            return jsonify(Error="Post not found."), 404
        elif not user:
            return jsonify(Error="User not found."), 404
        elif reply_text and p_replied and user_that_replied:
            ReplyDAO().insertReply(reply_text, p_replied, user_that_replied)
            result = self.build_reply_attributes(reply_text, p_replied, user_that_replied)
            return jsonify(Reply=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

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
