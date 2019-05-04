from flask import jsonify
from daos.chats import ChatsDAO
from handlers.users import UserHandler
from daos.users import UsersDAO


class ChatHandler:

    def build_chat_dict(self, row):
        chat_list = {'chat_id': row[0], 'chat_name': row[1], 'owner_id': row[2]}
        return chat_list

    def build_chat_attributes(self, chat_name, owner_id):
        result = {'chat_name': chat_name, 'owner_id': owner_id}
        return result

    def build_chat_owner_attributes(self, chat_name, first_name, last_name):
        result = {'user_id': chat_name, 'first_name': first_name, 'last_name': last_name}
        return result

    def getAllChats(self):
        dao = ChatsDAO()
        chat_list = dao.getAllChats()
        result_list = []
        for row in chat_list:
            result = self.build_chat_dict(row)
            result_list.append(result)
        return jsonify(Chat=result_list)

    def getChatById(self, chat_id):
        dao = ChatsDAO()
        row = dao.getChatById(chat_id)
        if not row:
            return jsonify(Error="Chat Not Found"), 404
        else:
            chat = self.build_chat_dict(row)
            return jsonify(Chat=chat)

    def getChatUsers(self, chat_id):
        dao = ChatsDAO()
        chat = dao.getChatById(chat_id)
        user_list = dao.getChatUsers(chat_id)
        if not user_list:
            return jsonify(Chat=user_list), 404
        elif not chat:
            return jsonify(Error="Chat not found"), 404
        else:
            result_list = []
            for row in user_list:
                user = UserHandler.build_user_dict(UserHandler, row)
                result_list.append(user)
            return jsonify(Chat=result_list)

    def getChatOwner(self, chat_id):
        chat = ChatsDAO().getChatById(chat_id)
        if not chat:
            return jsonify(Error="Chat Not Found"), 404
        else:
            result = ChatsDAO().getChatOwner(chat_id)
            result = self.build_chat_owner_attributes(result[0][0], result[0][1], result[0][2])
            return jsonify(Chat=result)

    def createChat(self, json):
        chat_name = json['chat_name']
        owner_id = json['owner_id']
        if chat_name and owner_id:
            dao = ChatsDAO()
            chat_id = dao.createChat(chat_name, owner_id)
            result = self.build_chat_attributes(chat_name, owner_id)
            return jsonify(Chat=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def removeChat(self, chat_id, owner_id):
        dao = ChatsDAO()
        o_id = dao.getChatOwner(chat_id)
        chat = dao.getChatById(chat_id)
        if owner_id != o_id[0][0]:
            return jsonify(Error="Operation invalid."), 404
        elif not chat:
            return jsonify(Error="Chat not found."), 404
        else:
            dao.removeChat(chat_id)
            return jsonify(DeleteStatus="OK"), 200

    def insertUserToChat(self, chat_id, user_id):
        dao = ChatsDAO()
        chat = dao.getChatById(chat_id)
        user = UsersDAO().getUserById(user_id)
        if not chat:
            return jsonify(Error="Chat not found."), 404
        elif not user:
            return jsonify(Error="User not found."), 404
        else:
            dao.insertUserToChat(chat_id, user_id)
            return jsonify(InsertStatus="OK"), 200

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

