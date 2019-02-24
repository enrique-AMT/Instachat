from flask import jsonify

class ChatHandler:
    def build_chat_dict(self, row):
        chat_list = {}
        chat_list['chat_id'] = row[0]
        chat_list['chat_name'] = row[1]
        chat_list['number_of_users'] = row[2]
        chat_list['user_id'] = row[3]
        chat_list['active_user_count'] = row[4]
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
        chats_list = [['1', 'test', '1', 'test1', '1']]
        result_list = []
        for row in chats_list:
            result = self.build_chat_dict(row)
            result_list.append(result)
        return jsonify(Chats=result_list)