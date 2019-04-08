from flask import jsonify
from daos.users import UsersDAO

class UserHandler:

    def build_user_dict(self, row):
        result = {'user_id': row[0], 'first_name': row[1], 'last_name': row[2]}
        return result

    def build_full_user_dict(self, row):
        result = {'user_id': row[0], 'first_name': row[1], 'last_name': row[2], 'u_email_address': row[3], 'phone': row[4]}
        return result

    def build_user_attributes(self, user_id, user_name, user_lastName, user_phone,user_contact_list,
                              user_email, user_password):

        result = {'user_id': user_id, 'user_name': user_name, 'user_lastName':user_lastName, 'user_phone': user_phone,
                  'user_contact_list': user_contact_list, 'user_email': user_email,'user_password': user_password}

        return result


    def getAllUsers(self):
        dao = UsersDAO()
        user_list = dao.getAllUsers()
        result_list = []
        for row in user_list:
          result = self.build_user_dict(row)
          result_list.append(result)
        return jsonify(User=result_list)

    def getUserById(self, user_id):
        dao = UsersDAO()
        return jsonify(Reply=dao.getUserById(user_id))

    def getUsersThatReact(self, post_id, react_type):
        dao = UsersDAO()
        user_list = dao.getUsersThatReact(post_id, react_type)
        if not user_list:
            return jsonify(Error="User not found"), 404
        else:
            return jsonify(Users=user_list)

    def createUser(self, json):
        print("TODO")
        # global uid
        # user_name = json['user_name']
        # user_lastName = json['user_lastName']
        # user_phone = json['user_phone']
        # user_contacts_list = json['user_contact_list']
        # user_email = json['user_email']
        # user_password = json['user_password']
        # if user_name and user_lastName and user_phone and user_contacts_list and user_email and user_password:
        #     print("added")
        #     user_list.append([{"user_id": uid, "user_name": user_name, "user_lastName": user_lastName,
        #                        "user_phone": user_phone, "user_contacts_list": user_contacts_list,
        #                        "user_email": user_email, "user_password": user_password}])
        #     result = self.build_user_attributes(uid, user_name, user_lastName, user_phone, user_contacts_list, user_email,
        #                                         user_password)
        #     uid = (uid + 1)
        #     return jsonify(User=result), 201
        # else:
        #     return jsonify(Error="Unexpected attributes in post request"), 400

    def updateUser(self, user_id, json):
        print("TODO")
        # if len(user_list) < user_id or user_id < 1:
        #     return jsonify(Error = "User not found."), 404
        # else:
        #     if len(json) != 7:
        #         return jsonify(Error = "Update request incorrect."), 400
        #     else:
        #         user_name = json['user_name']
        #         user_lastName = json['user_lastName']
        #         user_phone = json['user_phone']
        #         user_contacts_list = json['user_contact_list']
        #         user_email = json['user_email']
        #         user_password = json['user_password']
        #         if user_id and user_name and user_lastName and user_phone and user_contacts_list and user_email and user_password:
        #             return jsonify(UpdateStatus = "AREA TO UPDATE USER BY ID"), 200

    def deleteUser(self, user_id):
        print("TODO")
        # global uid
        # if len(user_list) < user_id or user_id < 1:
        #     return jsonify(Error = "User not found."), 404
        # else:
        #     return jsonify(DeleteStatus = "AREA TO DELETE USER BY ID"), 200


    def getUserContactList(self, user_id):
        dao = UsersDAO()
        contact_list = dao.getUserContactList(user_id)
        result_list = []
        for row in contact_list:
          result = self.build_user_dict(row)
          result_list.append(result)
        return jsonify(Contact=result_list)

    def getUserChatList(self, user_id):
        print("TODO")
        # if len(user_list) < user_id or user_id < 1:
        #     return jsonify(Error='User not found'), 404
        # else:
        #     return jsonify(User=user_list[user_id-1])
