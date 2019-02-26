from flask import jsonify

cid = 1

chats_list = [['1', 'test', '1', '[test1]', '1']]

class ChatHandler:


    def build_chat_dict(self, row):
        chat_list = {'chat_id': row[0], 'chat_name': row[1], 'number_of_users': row[2], 'user_id': row[3],
                     'active_user_count': row[4]}
        return chat_list

    def build_chat_attributes(self, chat_id, chat_name, number_of_users, user_id, active_user_count):
        result = {}
        result['chat_id'] = chat_id
        result['chat_name'] = chat_name
        result['number_of_users'] = number_of_users
        result['user_id'] = user_id
        result['active_user_count'] = active_user_count

        return result

    def getAllChats(self):
        result_list = []
        for row in chats_list:
            result = self.build_chat_dict(row)
            result_list.append(result)
        return jsonify(Chats=result_list)

    def getChatById(self, chat_id):
        if len(chats_list)< chat_id or chat_id<1:
            return jsonify(Error='Chat not found'), 404
        else:
            return jsonify(Chat=chats_list[chat_id-1])

    def createChat(self, json):
        global cid
        chat_name = json['chat_name']
        number_of_users = json['number_of_users']
        user_id = json['user_id']
        active_user_count = json['active_user_count']
        if chat_name and number_of_users and user_id and active_user_count:
            chat_id = (cid + 1)
            chats_list.append([chat_id, chat_name, number_of_users, user_id, active_user_count])
            result = self.build_chat_attributes(chat_id, chat_name, number_of_users, user_id, active_user_count)
            return jsonify(Chat=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateChat(self, chat_id, json):
        if len(chats_list) < chat_id or chat_id < 1:
            return jsonify(Error = "Reply not found."), 404
        else:
            if len(json) != 6:
                return jsonify(Error = "Update request incorrect."), 400
            else:
                chat_name = json['chat_name']
                number_of_users = json['number_of_users']
                user_id = json['user_id']
                active_user_count = json['active_user_count']
                if chat_name and number_of_users and user_id and active_user_count:
                    return jsonify(UpdateStatus = "AREA TO UPDATE SESSION BY ID"), 200

    def deleteChat(self, chat_id):
        global p_id
        if len(chats_list) < chat_id or chat_id < 1:
            return jsonify(Error = "Session not found."), 404
        else:
            return jsonify(DeleteStatus = "AREA TO DELETE SESSION BY ID"), 200
