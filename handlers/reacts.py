from config.dbconfig import pg_config
import psycopg2
from flask import jsonify
from daos.reacts import ReactsDAO
from daos.posts import PostsDAO

class ReactHandler:

    def build_react_dict(self, row):
        react_list = {'react_id': row[0], 'react_type': row[1], 'react_date': row[2]}
        return react_list

    def build_react_attributes(self, react_id, react_type, react_date):
        result = {'react_id': react_id, 'react_type': react_type, 'react_date': react_date}

        return result

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
        return jsonify(React=dao.getReactById(react_id))

    def getReactByDate(self, react_date):
        dao = ReactsDAO()
        return jsonify(React=dao.getReactByDate(react_date))

    def getReactsOnPost(self, post_id, react_type):
        dao = ReactsDAO()
        PostsDAO().getPostById(post_id)
        return jsonify(React=dao.getReactsOnPost(post_id, react_type))

    def createReact(self):
      print("TODO")

    def updateReact(self):
      print("TODO")

    def deleteReact(self):
      print("TODO")

