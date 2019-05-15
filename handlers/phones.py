from flask import jsonify
from daos.chats import ChatsDAO
from handlers.users import UserHandler
from daos.users import UsersDAO
from daos.phones import PhonesDAO


class PhonesHandler:

    def build_phone_dict(self, row):
        chat_list = {'phone_id': row[0], 'u_phone': row[1], 'phone': row[2]}
        return chat_list

    def build_phone_attributes(self, u_phone, phone):
        result = {'u_phone': u_phone, 'phone': phone}
        return result

    def getAllPhone(self):
        dao = PhonesDAO()
        phone_list = dao.getPhones()
        result_list = []
        for row in phone_list:
            result = self.build_phone_dict(row)
            result_list.append(result)
        return jsonify(Phone=result_list)

    def getPhoneById(self, user_id):
        dao = PhonesDAO()
        row = UsersDAO().getUserById(user_id)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            result = dao.getPhoneById(user_id)
            phone = self.build_phone_attributes(result)
            return jsonify(Phone=phone)

    def createPhone(self, json):
        u_phone = json['u_phone']
        phone = json['phone']
        if u_phone and phone:
            dao = PhonesDAO()
            phone_id = dao.createPhone(u_phone, phone)
            result = self.build_phone_attributes(u_phone, phone)
            return jsonify(Phone=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


