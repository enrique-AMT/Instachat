from flask import jsonify

uid = 2
user_list = [[1, 'Juan', 'Del Pueblo', '787-777-7777', ['2', '3', '4']]]
class UserHandler:

    def build_user_dict(self, row):
        result = {'user_id': row[0], 'user_name': row[1], 'user_lastName': row[2], 'user_phone': row[3],
                     'user_contact_list': row[4]}
        return result

    def build_user_attributes(self, user_id, user_name, user_lastName, user_phone,user_contact_list, ):
        result = {}
        result['user_id'] = user_id
        result['user_name'] = user_name
        result['user_lastName'] = user_lastName
        result['user_phone'] = user_phone
        result['user_contact_list'] = user_contact_list

        return result

    def getAllUsers(self):
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def getUserById(self, user_id):
        if len(user_list) < user_id or user_id < 1:
            return jsonify(Error='User not found'), 404
        else:
            return jsonify(User=user_list[user_id-1])

    def createUser(self, json):
        global uid
        user_name = json['user_name']
        user_lastName = json['user_lastName']
        user_phone = json['user_phone']
        user_contacts_list = json['user_contact_list']
        if user_name and user_lastName and user_phone and user_contacts_list:
            print("added")
            user_list.append([uid, user_name, user_lastName, user_phone, user_contacts_list])
            result = self.build_user_attributes(uid, user_name, user_lastName, user_phone, user_contacts_list)
            uid = (uid + 1)
            return jsonify(User=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateUser(self, user_id, json):
        if len(user_list) < user_id or user_id < 1:
            return jsonify(Error = "User not found."), 404
        else:
            if len(json) != 5:
                return jsonify(Error = "Update request incorrect."), 400
            else:
                user_name = json['user_name']
                user_lastName = json['user_lastName']
                user_phone = json['user_phone']
                user_contacts_list = json['user_contact_list']
                if user_id and user_name and user_lastName and user_phone and user_contacts_list:
                    return jsonify(UpdateStatus = "AREA TO UPDATE USER BY ID"), 200

    def deleteUser(self, user_id):
        global uid
        if len(user_list) < user_id or user_id < 1:
            return jsonify(Error = "User not found."), 404
        else:
            return jsonify(DeleteStatus = "AREA TO DELETE USER BY ID"), 200
