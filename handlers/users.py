from flask import jsonify
from daos.users import UsersDAO


class UserHandler:

    def build_user_dict(self, row):
        result = {'user_id': row[0], 'first_name': row[1], 'last_name': row[2]}
        return result

    def build_user_react_dict(self, row):
        result = {'user_id': row[0], 'first_name': row[1], 'last_name': row[2], 'react_date': row[3]}
        return result

    def build_user_chat_dict(self,row):
        chat_list = {'chat_id': row[0], 'chat_name': row[1], 'owner_id': row[2]}
        return chat_list

    def build_active_user_dict(self,row):
        chat_list = {'post_date':row[0], 'username': row[1], 'post_count': row[2]}
        return chat_list

    def build_removed_user_dict(self, row):
        result = {'username': row[0], 'chat_name': row[1]}

    def build_full_user_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['u_email_address'] = row[3]
        result['u_password'] = row[4]
        result['username'] = row[5]
        if row[6]:
            result['phone'] = row[6]

        return result

    def build_phone_attributes(self, user_id, phone):
        result = {'user_id':user_id, 'phone':phone}

    def build_user_attributes(self, first_name, last_name, u_email_address, u_password, username):

        result = {'first_name': first_name, 'last_name': last_name,
                  'u_email_address': u_email_address, 'u_password': u_password, 'username': username}

        return result

    def createUser(self, json):
        first_name = json['first_name']
        last_name = json['last_name']
        u_email_address = json['u_email_address']
        u_password = json['u_password']
        username = json['username']
        if first_name and last_name and u_email_address and u_password and username:
            UsersDAO().createUser(first_name, last_name, u_email_address, u_password, username)
            result = self.build_user_attributes(first_name, last_name, u_email_address, u_password, username)
            return jsonify(User=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def getAllUsers(self):
        dao = UsersDAO()
        user_list = dao.getAllUsers()
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def getDetailedUsers(self):
        dao = UsersDAO()
        user_list = dao.getDetailedUsers()
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(User=result_list)

    def getUserById(self, user_id):
        dao = UsersDAO()
        row = dao.getUserById(user_id)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_full_user_dict(row)
            return jsonify(User=user)

    def getUserByUsername(self, username):
        dao = UsersDAO()
        row = dao.getUserByUsername(username)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_full_user_dict(row)
            return jsonify(User=user)

    def getUsersThatReact(self, post_id, react_type):
        dao = UsersDAO()
        user_list = dao.getUsersThatReact(post_id, react_type)
        if not user_list:
            return jsonify(Error="User not found"), 404
        else:
            result_list = []
            for row in user_list:
                result = self.build_user_react_dict(row)
                result_list.append(result)
            return jsonify(User=result_list)

    def getUserContactList(self, user_id):
        dao = UsersDAO()
        row = dao.getUserById(user_id)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            contact_list = dao.getUserContactList(user_id)
            result_list = []
            for row in contact_list:
                result = self.build_user_dict(row)
                result_list.append(result)
            return jsonify(Contact=result_list)

    def getUserChatList(self, user_id):
        dao = UsersDAO()
        user = dao.getUserById(user_id)
        if not user:
            print("UNFH")
            return jsonify(Error="User not found."), 404
        else:
            chat_list = dao.getUserChats(user_id)
            result_list = []
            for row in chat_list:
                result = self.build_user_chat_dict(row)
                result_list.append(result)
            return jsonify(Chat=result_list)

    def removeUserFromChat(self, user_id, chat_id):
        dao = UsersDAO()
        row = dao.checkUsersOnChat(user_id, chat_id)
        if not row:
            return jsonify(Error="Request cannot be completed"), 404
        else:
            dao.removeUserFromChat(user_id, chat_id)
            return jsonify(DeleteStatus="OK"), 200

    def removeUserFromContacts(self, user_id, contact_id):
        dao = UsersDAO()
        row = dao.checkUserContacts(user_id, contact_id)
        if not row:
            return jsonify(Error="Request cannot be completed"), 404
        else:
            dao.removeUserFromContacts(user_id, contact_id)
            return jsonify(DeleteStatus="OK"), 200

    def insertUserToContacts(self, user_id, contact_id):
        dao = UsersDAO()
        user = UsersDAO().getUserById(user_id)
        contact = UsersDAO().getUserById(contact_id)
        if not user:
            return jsonify(Error="User not found."), 404
        elif not contact:
            return jsonify(Error="User not found."), 404
        else:
            dao.insertUserToContacts(user_id, contact_id)
            return jsonify(InsertStatus="OK"), 200

    def login(self, json):
        username = json['username']
        password = json['password']
        user = UsersDAO().getUserByUsername(username)
        if not user:
            return jsonify(Error="User not found"), 404
        elif username and password:
            result = UsersDAO().login(username, password)
            if not result:
                return jsonify(Error="Bad combination of username and password."), 404
            else:
                return jsonify(Login=result)
    def getActiveUsers(self):
        dao = UsersDAO()
        user = dao.getActiveUsers()
        if not user:
          return jsonify(Error="No active users.")
        else:
          result_list = []
          for row in user:
            result = self.build_active_user_dict(row)
            result_list.append(result)
          return jsonify(User=result_list)

    def insertPhone(self, json):
      user_id=json['user_id']
      phone=json['phone']
      dao = UsersDAO()
      if user_id and phone:
        phone_id = dao.insertPhone(user_id, phone)
        result = self.build_phone_attributes(user_id, phone)
        return jsonify(Phone=result), 201
      else:
        return jsonify(Error="Unexpected attributes in post request"), 400


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

