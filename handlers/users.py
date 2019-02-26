from flask import jsonify

uid = 1
user_list = [['1', 'Juan', 'Del Pueblo', '787-777-7777', ['2', '3', '4'], 'dummy@gmail.com', 'dummy1234']]
class UserHandler:

    def build_user_dict(self, row):
        result = {'user_id': row[0], 'user_name': row[1], 'user_lastName': row[2], 'user_phone': row[3],
                     'user_contact_list': row[4], 'user_email': row[5], 'user_password': row[6]}
        return result

    def build_user_attributes(self, user_id, user_name, user_lastName, user_phone,user_contact_list, user_email, user_password ):
        result = {}
        result['user_id'] = user_id
        result['user_name'] = user_name
        result['user_lastName'] = user_lastName
        result['user_phone'] = user_phone
        result['user_contact_list'] = user_contact_list
        result['user_email'] = user_email
        result['user_password'] = user_password


        return result

    def getAllUsers(self):
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def getUserById(self, user_id):
        if len(user_list) < user_id or user_id<1:
            return jsonify(Error='User not found'), 404
        else:
            return jsonify(User=user_list[user_id-1])


    def createUser(self, json):
        global uid
        user_id = json['user_id']
        user_name = json['user_name']
        user_lastName = json['user_lastName']
        user_phone = json['user_phone']
        user_contacts_list = json['user_contact_list']
        user_email = json['user_email']
        user_password = json['user_password']
        if user_id and user_name and user_lastName and user_phone and user_contacts_list and user_email and user_password:
            print("added")
            user_id = (uid + 1)
            user_list.append([user_id, user_name, user_lastName, user_phone, user_contacts_list, user_email, user_password])
            result = self.build_user_attributes(user_id, user_name, user_lastName, user_phone, user_contacts_list ,user_email, user_password)
            return jsonify(User=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def updateUser(self, user_id, json):
        if len(user_list) < user_id:
            return jsonify(Error = "User not found."), 404
        else:
            if len(json) != 9:
                return jsonify(Error = "Update request incorrect."), 400
            else:
                user_id = json['user_id']
                user_name = json['user_name']
                user_lastName = json['user_lastName']
                user_phone = json['user_phone']
                user_contacts_list = json['user_contacts_list']
                user_email = json['user_email']
                user_password = json['user_password']
                if user_id and user_name and user_lastName and user_phone and user_contacts_list and user_email and user_password:
                    return jsonify(UpdateStatus = "AREA TO UPDATE POST BY ID"), 200

    def deletePost(self, user_id):
        global uid
        if len(user_list) < user_id or user_id < 1:
            return jsonify(Error = "User not found."), 404
        else:
            return jsonify(DeleteStatus = "AREA TO DELETE POST BY ID"), 200
