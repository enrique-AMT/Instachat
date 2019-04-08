from flask import jsonify
from daos.chats import ChatsDAO
from handlers.users import UserHandler

class ChatHandler:


    def build_chat_dict(self, row):
        chat_list = {'chat_id': row[0], 'chat_name': row[1], 'owner_id': row[2]}
        return chat_list

    def build_chat_attributes(self, chat_name, owner_id):
        result = {'chat_name': chat_name, 'owner_id': owner_id}

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
            return jsonify(Error="Users Not Found"), 404
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
            return jsonify(Chat=ChatsDAO().getChatOwner(chat_id))

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
