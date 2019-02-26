from flask import jsonify

uid = 1
class UserHandler:

    def build_user_dict(self, row):
        user_list = {'user_id': row[0], 'user_name': row[1], 'user_lastName': row[2], 'user_phone': row[3],
                     'user_contact_list': row[4]}
        return user_list

    def build_user_attributes(self, user_id, user_name, user_lastName, user_phone,user_contact_list, ):
        result = {}
        result['user_id'] = user_id
        result['user_name'] = user_name
        result['user_lastName'] = user_lastName
        result['user_phone'] = user_phone
        result['user_contact_list'] = user_contact_list

        return result

    def getAllUsers(self):
        user_list = [['1', 'Juan', 'Del Pueblo', '787-777-7777', ['2', '3', '4']]]
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def createUser(self, json):
        global uid
        users_list = [['1', 'Juan', 'Del Pueblo', '787-777-7777', ['2', '3', '4']]]
        user_id = json['user_id']
        user_name = json['user_name']
        user_lastName = json['user_lastName']
        user_phone = json['user_phone']
        user_contacts_list = json['user_contact_list']
        if user_id and user_name and user_lastName and user_phone and user_contacts_list:
            user_id = (uid + 1)
            users_list.append([user_id, user_name, user_lastName, user_phone, user_contacts_list])
            result = self.build_user_attributes(user_id, user_name, user_lastName, user_phone, user_contacts_list)
            return jsonify(Part=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400
