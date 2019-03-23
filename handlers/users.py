from flask import jsonify

uid = 2
user_list = [{"user_id": 1, "user_name": "Juan", "user_lastName": "Del Pueblo", "user_phone": "787-777-7777",
              "user_contact_list": '["1","3","4"]', "user_email": "dummy@gmail.com", "user_password": "dummy1234"}]
class UserHandler:

    def build_user_dict(self, row):
        result = {'user_id': row[0], 'user_name': row[1], 'user_lastName': row[2], 'user_phone': row[3],
                     'user_contact_list': row[4], 'user_email': row[5], 'user_password': row[6]}
        return result

    def build_user_attributes(self, user_id, user_name, user_lastName, user_phone,user_contact_list,
                              user_email, user_password):

        result = {'user_id': user_id, 'user_name': user_name, 'user_lastName':user_lastName, 'user_phone': user_phone,
                  'user_contact_list': user_contact_list, 'user_email': user_email,'user_password': user_password}

        return result


    def getAllUsers(self):
        return jsonify(User=user_list)

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
        user_email = json['user_email']
        user_password = json['user_password']
        if user_name and user_lastName and user_phone and user_contacts_list and user_email and user_password:
            print("added")
            user_list.append([{"user_id": uid, "user_name": user_name, "user_lastName": user_lastName,
                               "user_phone": user_phone, "user_contacts_list": user_contacts_list,
                               "user_email": user_email, "user_password": user_password}])
            result = self.build_user_attributes(uid, user_name, user_lastName, user_phone, user_contacts_list, user_email,
                                                user_password)
            uid = (uid + 1)
            return jsonify(User=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateUser(self, user_id, json):
        if len(user_list) < user_id or user_id < 1:
            return jsonify(Error = "User not found."), 404
        else:
            if len(json) != 7:
                return jsonify(Error = "Update request incorrect."), 400
            else:
                user_name = json['user_name']
                user_lastName = json['user_lastName']
                user_phone = json['user_phone']
                user_contacts_list = json['user_contact_list']
                user_email = json['user_email']
                user_password = json['user_password']
                if user_id and user_name and user_lastName and user_phone and user_contacts_list and user_email and user_password:
                    return jsonify(UpdateStatus = "AREA TO UPDATE USER BY ID"), 200

    def deleteUser(self, user_id):
        global uid
        if len(user_list) < user_id or user_id < 1:
            return jsonify(Error = "User not found."), 404
        else:
            return jsonify(DeleteStatus = "AREA TO DELETE USER BY ID"), 200


    def getUserContactList(self, user_id):
        if len(user_list) < user_id or user_id < 1:
            return jsonify(Error='User not found'), 404
        else:
            return jsonify(User=user_list[user_id-1])

    def getUserChattList(self, user_id):
        if len(user_list) < user_id or user_id < 1:
            return jsonify(Error='User not found'), 404
        else:
            return jsonify(User=user_list[user_id-1])
