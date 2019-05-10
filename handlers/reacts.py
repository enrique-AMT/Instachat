from config.dbconfig import pg_config
import psycopg2
from flask import jsonify
from daos.reacts import ReactsDAO
from daos.posts import PostsDAO
from daos.users import UsersDAO
from daos.reply import ReplyDAO


class ReactHandler:

    def build_react_dict(self, row):
        react_list = {'react_id': row[0], 'react_type': row[1], 'react_date': row[2], 'user_that_react': row[3],
                      'p_reacted': row[4], 'reply_reacted': row[5]}
        return react_list

    def build_like_count_dict(self, row):
        result = {'post_id': row[0], 'Total_of_likes': row[1]}
        return result

    def build_dislike_count_dict(self, row):
        result = {'post_id': row[0], 'Total_of_dislikes': row[1]}
        return result

    def build_react_attributes_P(self, react_type, user_that_react, p_reacted):
        result = {'react_type': react_type, 'user_that_react': user_that_react,
                  'p_reacted': p_reacted}
        return result

    def build_react_attributes_R(self, react_type, user_that_react, reply_reacted):
        result = {'react_type': react_type, 'user_that_react': user_that_react,
                  'reply_reacted': reply_reacted}
        return result

    def insertReact(self, json):
        react_type = json['react_type']
        user_that_react = json['user_that_react']
        p_reacted = -1
        reply_reacted = -1
        user = UsersDAO().getUserById(user_that_react)
        if json.get('p_reacted'):
            p_reacted = json['p_reacted']
            post = PostsDAO().getPostById(p_reacted)
            if not post:
                return jsonify(Error="Post not found."), 404
        elif json.get('reply_reacted'):
            reply_reacted = json['reply_reacted']
            reply = ReplyDAO().getReplyById(reply_reacted)
            if not reply:
                return jsonify(Error="Reply not found."), 404

        if not user:
            return jsonify(Error="User not found."), 404
        elif react_type and user_that_react and json.get('p_reacted'):
            ReactsDAO().insertReactP(react_type, user_that_react, p_reacted)
            result = self.build_react_attributes_P(react_type, user_that_react, p_reacted)
            return jsonify(React=result), 201
        elif react_type and user_that_react and json.get('reply_reacted'):
            ReactsDAO().insertReactR(react_type, user_that_react, reply_reacted)
            result = self.build_react_attributes_R(react_type, user_that_react, reply_reacted)
            return jsonify(React=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def getAllReacts(self):
        dao = ReactsDAO()
        react_list = dao.getAllReacts()
        result_list = []
        for row in react_list:
            result = self.build_react_dict(row)
            result_list.append(result)
        return jsonify(React=result_list)

    def getReactById(self, react_id):
        dao = ReactsDAO()
        row = dao.getReactById(react_id)
        if not row:
            return jsonify(Error="React not found."), 404
        else:
            react = self.build_react_dict(row)
            return jsonify(React=react)

    def getReactByDate(self, react_date):
        dao = ReactsDAO()
        return jsonify(React=dao.getReactByDate(react_date))

    def getReactsOnPost(self, post_id, react_type):
        dao = ReactsDAO()
        reacts = dao.getReactsOnPost(post_id, react_type)
        if not reacts:
            return jsonify(Reacts=reacts), 404
        else:
            result_list = []
            for row in reacts:
                if react_type == 'like':
                    result = self.build_like_count_dict(row)
                    result_list.append(result)
                elif react_type == 'dislike':
                    result = self.build_dislike_count_dict(row)
                    result_list.append(result)
            return jsonify(Reacts=result_list)

    def getReactsOnReplies(self, reply_id, react_type):
        dao = ReactsDAO()
        reacts = dao.getReactsOnReplies(reply_id, react_type)
        if not reacts:
            return jsonify(Reacts=reacts), 404
        else:
            result_list = []
            for row in reacts:
                if react_type == 'like':
                    result = self.build_like_count_dict(row)
                    result_list.append(result)
                elif react_type == 'dislike':
                    result = self.build_dislike_count_dict(row)
                    result_list.append(result)
            return jsonify(Reacts=result_list)

    def updateReact(self):
      print("TODO")

    def deleteReact(self):
      print("TODO")

