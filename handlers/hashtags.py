from flask import jsonify
from daos.hashtags import HashtagsDAO

class HashtagsHandler:


    def build_hashtag_dict(self, row):
        hashtag_list = {'hashtag_id': row[0], 'hash_name': row[1]}
        return hashtag_list

    def build_daily_hashtag_dict(self, row, index):
        hashtag_list = {'hashtag_id': row[0], 'hash_name': row[1], 'position': index}
        return hashtag_list

    def build_chat_attributes(self, chat_name, number_of_users, owner_id):
        result = {'chat_name': chat_name, 'number_of_users': number_of_users, 'owner_id': owner_id}

        return result

    def getAllHashtags(self):
        dao = HashtagsDAO()
        chat_list = dao.getAllHashtags()
        result_list = []
        for row in chat_list:
          result = self.build_hashtag_dict(row)
          result_list.append(result)
        return jsonify(Hashtag=result_list)

    def getHashtagById(self, chat_id):
        dao = HashtagsDAO()
        row = dao.getChatById(chat_id)
        if not row:
          return jsonify(Error="Hashtag Not Found"), 404
        else:
          chat = self.build_hashtag_dict(row)
          return jsonify(Hashtag=chat)

    def getDailyHashtags(self, post_date):
      dao = HashtagsDAO()
      post_date = post_date[0:2]+ "/" + post_date[2:4] + "/" + post_date[-4:]
      print(post_date)
      hashtag_list = dao.getDailyHashtags(post_date)
      if not post_date:
        return jsonify(Error="Session Not Found"), 404
      else:
        result_list = []
        for index, row in enumerate(hashtag_list, start=1):
          position = self.build_daily_hashtag_dict(row, index)
          result_list.append(position)
        return jsonify(Hashtag=result_list)

    def createChat(self, json):
      print("todo")
        # global cid
        # chat_name = json['chat_name']
        # number_of_users = json['number_of_users']
        # user_id = json['user_id']
        # active_user_count = json['active_user_count']
        # owner_id = json['owner_id']
        # if chat_name and number_of_users and user_id and active_user_count and owner_id:
        #     chats_list.append(
        #         {'chat_id': cid, 'chat_name': chat_name, 'number_of_users': number_of_users, 'user_id':
        #             user_id, 'active_user_count': active_user_count, 'owner_id': owner_id})
        #     result = self.build_chat_attributes(cid, chat_name, number_of_users, user_id, active_user_count, owner_id)
        #     cid = (cid + 1)
        #     return jsonify(Chat=result), 201
        # else:
        #     return jsonify(Error="Unexpected attributes in post request"), 400

    def updateChat(self, chat_id, json):
      print("todo")
        # if len(chats_list) < chat_id or chat_id < 1:
        #     return jsonify(Error = "Chat not found."), 404
        # else:
        #     if len(json) != 5:
        #         return jsonify(Error = "Update request incorrect."), 400
        #     else:
        #         chat_name = json['chat_name']
        #         number_of_users = json['number_of_users']
        #         user_id = json['user_id']
        #         active_user_count = json['active_user_count']
        #         owner_id = json['owner_id']
        #         if chat_name and number_of_users and user_id and active_user_count and owner_id:
        #             return jsonify(UpdateStatus = "AREA TO UPDATE CHAT BY ID"), 200

    def deleteChat(self, chat_id):
      print("todo")
        # global cid
        # if len(chats_list) < chat_id or chat_id < 1:
        #     return jsonify(Error = "Chat not found."), 404
        # else:
        #     return jsonify(DeleteStatus = "AREA TO DELETE CHAT BY ID"), 200
