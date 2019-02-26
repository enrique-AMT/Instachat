from flask import Flask, jsonify, request
from handlers.chats import ChatHandler
from handlers.posts import PostHandler
from handlers.sessions import SessionHandler


# from flask_cors import CORS, cross_origin


app = Flask(__name__)
@app.route('/')
def greeting():
    return 'Welcome to the poor mans Instagram!'


@app.route('/InstaChat/chats', methods=['GET', 'POST'])
def getAllParts():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().createChat(request.json)
    else:
        if not request.args:
            return ChatHandler().getAllChats()
        else:
            return


@app.route('/InstaChat/posts', methods=['POST', 'GET'])
def getAllPost():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PostHandler().insertPostJson(request.json)
    else:
        if not request.args:
            return PostHandler().getAllPosts()


@app.route('/InstaChat/posts/<int:post_id>', methods=['GET', 'PUT', 'DELETE'])
def getPostById(post_id):
    if request.method == 'GET':
        return PostHandler().getPostById(post_id)
    elif request.method == 'PUT':
        return PostHandler().updatePost(post_id, request.json)
    elif request.method == 'DELETE':
        return PostHandler().deletePost(post_id)
    else:
        return jsonify(Error = "Method not allowed."), 405


@app.route('/InstaChat/sessions', methods=['POST', 'GET'])
def getAllSessions():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return SessionHandler().insertSessionJson(request.json)
    else:
        if not request.args:
            return SessionHandler().getAllSessions()


@app.route('/InstaChat/sessions/<int:session_id>', methods=['GET', 'PUT', 'DELETE'])
def getSessionById(session_id):
    if request.method == 'GET':
        return SessionHandler().getSessionById(session_id)
    elif request.method == 'PUT':
        return SessionHandler().updateSession(session_id, request.json)
    elif request.method == 'DELETE':
        return SessionHandler().deleteSession(session_id)
    else:
        return jsonify(Error = "Method not allowed."), 405


if __name__ == '__main__':
    app.run()
