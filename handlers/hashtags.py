from flask import jsonify
from daos.hashtags import HashtagsDAO
from daos.posts import PostsDAO


class HashtagsHandler:

    def build_hashtag_dict(self, row):
        hashtag_list = {'hashtag_id': row[1], 'hash_name': row[0]}
        return hashtag_list

    def build_daily_hashtag_dict(self, row, index):
        hashtag_list = {'hash_name': row[0], 'hashtag_count': row[1], 'position': index}
        return hashtag_list

    def build_hashtag_attributes(self, hashtag_id, hash_name):
        hashtag_list = {'hashtag_id': hashtag_id, 'hash_name': hash_name}
        return hashtag_list

    def build_hashtag_Post(self, post_id, hashtag_id):
        hashtag_list = {'p_with_hashtag': post_id, 'hashtag_id': hashtag_id}
        return hashtag_list

    def build_chat_attributes(self, chat_name, number_of_users, owner_id):
        result = {'chat_name': chat_name, 'number_of_users': number_of_users, 'owner_id': owner_id}

        return result

    def getAllHashtags(self):
        dao = HashtagsDAO()
        hashtag_list = dao.getAllHashtags()
        result_list = []
        for row in hashtag_list:
            result = self.build_hashtag_dict(row)
            result_list.append(result)
        return jsonify(Hashtag=result_list)

    def getHashtagsPostX(self, post_id):
      dao = HashtagsDAO()
      hashtag_list = dao.getHashtahPostX(post_id)
      result_list = []
      for row in hashtag_list:
        result = self.build_hashtag_dict(row)
        result_list.append(result)
      return jsonify(Hashtag=result_list)

    def getHashtagById(self, chat_id):
        dao = HashtagsDAO()
        row = dao.getHashtagById(chat_id)
        if not row:
            return jsonify(Error="Hashtag Not Found"), 404
        else:
            chat = self.build_hashtag_dict(row)
            return jsonify(Hashtag=chat)

    def getDailyHashtags(self, post_date):
      dao = HashtagsDAO()
      hashtag_list = dao.getDailyHashtags(post_date)
      if not post_date:
        return jsonify(Error="Session Not Found"), 404
      else:
        result_list = []
        for index, row in enumerate(hashtag_list, start=1):
          position = self.build_daily_hashtag_dict(row, index)
          result_list.append(position)
        return jsonify(Hashtag=result_list)

    def createHashtag(self, json):
        hash_name = json['hash_name']
        if hash_name:
            hashtag = HashtagsDAO().createHashtag(hash_name)
            result = self.build_hashtag_attributes(hashtag, hash_name)
            return jsonify(Post=result), 201
        else:
            return jsonify(Error="Unexpected attributes in hashtag request"), 400

    def insertHashtagToPost(self, json):
        p_with_hashtag = json['p_with_hashtag']
        hashtag_id = json['hashtag_id']
        post = PostsDAO().getPostById(p_with_hashtag)
        hashtag = HashtagsDAO().getHashtagById(hashtag_id)
        if not post:
            return jsonify(Error="Post not found."), 404
        elif not hashtag:
            return jsonify(Error="Hashtag not found."), 404
        elif p_with_hashtag and hashtag_id:
            HashtagsDAO().insertHashtagToPost(p_with_hashtag, hashtag_id)
            result = self.build_hashtag_Post(p_with_hashtag, hashtag_id)
            return jsonify(Has_Hashatg=result)
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


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
