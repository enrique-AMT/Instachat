from flask import jsonify

cid = 2

chats_list = [{'chat_id': 1, 'chat_name': 'test','number_of_users': '1','user_id':
                '[1]','active_user_count': '1','owner_id': '258'}]

class ChatHandler:


    def build_chat_dict(self, row):
        chat_list = {'chat_id': row[0], 'chat_name': row[1], 'number_of_users': row[2], 'user_id': row[3],
                     'active_user_count': row[4], 'owner_id': row[5]}
        return chat_list

    def build_chat_attributes(self, chat_id, chat_name, number_of_users, user_id, active_user_count, owner_id):
        result = {'chat_id': chat_id, 'chat_name': chat_name, 'number_of_users': number_of_users, 'user_id': user_id,
                  'active_user_count': active_user_count, 'owner_id': owner_id}

        return result

    def getAllChats(self):
        return jsonify(Chats=chats_list)

    def getChatById(self, chat_id):
        if len(chats_list) < chat_id or chat_id < 1:
            return jsonify(Error='Chat not found'), 404
        else:
            return jsonify(Chat=chats_list[chat_id-1])

    def createChat(self, json):
        global cid
        chat_name = json['chat_name']
        number_of_users = json['number_of_users']
        user_id = json['user_id']
        active_user_count = json['active_user_count']
        owner_id = json['owner_id']
        if chat_name and number_of_users and user_id and active_user_count and owner_id:
            chats_list.append(
                {'chat_id': cid, 'chat_name': chat_name, 'number_of_users': number_of_users, 'user_id':
                    user_id, 'active_user_count': active_user_count, 'owner_id': owner_id})
            result = self.build_chat_attributes(cid, chat_name, number_of_users, user_id, active_user_count, owner_id)
            cid = (cid + 1)
            return jsonify(Chat=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateChat(self, chat_id, json):
        if len(chats_list) < chat_id or chat_id < 1:
            return jsonify(Error = "Chat not found."), 404
        else:
            if len(json) != 5:
                return jsonify(Error = "Update request incorrect."), 400
            else:
                chat_name = json['chat_name']
                number_of_users = json['number_of_users']
                user_id = json['user_id']
                active_user_count = json['active_user_count']
                owner_id = json['owner_id']
                if chat_name and number_of_users and user_id and active_user_count and owner_id:
                    return jsonify(UpdateStatus = "AREA TO UPDATE CHAT BY ID"), 200

    def deleteChat(self, chat_id):
        global cid
        if len(chats_list) < chat_id or chat_id < 1:
            return jsonify(Error = "Chat not found."), 404
        else:
            return jsonify(DeleteStatus = "AREA TO DELETE CHAT BY ID"), 200
