from flask import Flask, jsonify, request
from handlers.chats import ChatHandler
from handlers.posts import PostHandler
from handlers.sessions import SessionHandler
from handlers.users import UserHandler
from handlers.reply import ReplyHandler

app = Flask(__name__)


@app.route('/')
def greeting():
    return 'Welcome to InstaChat!'


@app.route('/InstaChat/chats', methods=['GET', 'POST'])
def getAllChats():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().createChat(request.json)
    else:
        if not request.args:
            return ChatHandler().getAllChats()
        else:
            return


@app.route('/InstaChat/chats/<int:chat_id>', methods=['GET', 'PUT', 'DELETE'])
def getChatById(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatById(chat_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/users', methods=['POST', 'GET'])
def getAllUsers():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return UserHandler().createUser(request.json)
    else:
        if not request.args:
            return UserHandler().getAllUsers()


@app.route('/InstaChat/users/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def getUserById(user_id):
    if request.method == 'GET':
        return UserHandler().getUserById(user_id)
    elif request.method == 'PUT':
        return UserHandler().updateUser(user_id, request.json)
    elif request.method == 'DELETE':
        return UserHandler().deleteUser(user_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/replies', methods=['POST', 'GET'])
def getAllReplies():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ReplyHandler().createReply(request.json)
    else:
        if not request.args:
            return ReplyHandler().getAllReplies()


@app.route('/InstaChat/replies/<int:reply_id>', methods=['GET', 'PUT', 'DELETE'])
def getReplyById(reply_id):
    if request.method == 'GET':
        return ReplyHandler().getReplyById(reply_id)
    elif request.method == 'PUT':
        return ReplyHandler().updateReply(reply_id, request.json)
    elif request.method == 'DELETE':
        return ReplyHandler().deleteReply(reply_id)
    else:
        return jsonify(Error="Method not allowed."), 405


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
