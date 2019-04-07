from flask import Flask, jsonify, request
from handlers.chats import ChatHandler
from handlers.posts import PostHandler
# from handlers.sessions import SessionHandler
from handlers.users import UserHandler
from handlers.reply import ReplyHandler
from handlers.hashtags import HashtagsHandler
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


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

@app.route('/InstaChat/dashboard/<string:post_date>/hashtags', methods=['GET', 'POST'])
def getDailyHashtags(post_date):
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().createChat(request.json)
    else:
        if not request.args:
            return HashtagsHandler().getDailyHashtags(post_date)
        else:
            return

@app.route('/InstaChat/dashboard/posts', methods=['GET', 'POST'])
def getDailyPosts():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().createChat(request.json)
    else:
        if not request.args:
            return PostHandler().getDailyPosts()
        else:
            return


@app.route('/InstaChat/chats/<int:chat_id>', methods=['GET', 'PUT', 'DELETE'])
def getChatById(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatById(chat_id)
    elif request.method == 'PUT':
        return ChatHandler().updateChat(chat_id, request.json)
    elif request.method == 'DELETE':
        return ChatHandler().deleteChat(chat_id)
    else:
        return jsonify(Error = "Method not allowed."), 405

@app.route('/InstaChat/chats/<int:chat_id>/posts', methods=['GET', 'PUT', 'DELETE'])
def getAllPosts(chat_id):
    if request.method == 'GET':
        return PostHandler().getChatPosts(chat_id)
    elif request.method == 'PUT':
        return ChatHandler().updateChat(chat_id, request.json)
    elif request.method == 'DELETE':
        return ChatHandler().deleteChat(chat_id)
    else:
        return jsonify(Error = "Method not allowed."), 405

@app.route('/InstaChat/chats/<int:chat_id>/users', methods=['GET', 'PUT', 'DELETE'])
def getChatUsers(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatUsers(chat_id)
    elif request.method == 'PUT':
        return ChatHandler().updateChat(chat_id, request.json)
    elif request.method == 'DELETE':
        return ChatHandler().deleteChat(chat_id)
    else:
        return jsonify(Error = "Method not allowed."), 405


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
        return jsonify(Error = "Method not allowed."), 405

@app.route('/InstaChat/users/<int:user_id>/contacts', methods=['GET', 'PUT', 'DELETE'])
def getUserContactList(user_id):
    if request.method == 'GET':
        return UserHandler().getUserContactList(user_id)
    elif request.method == 'PUT':
        return UserHandler().updateUser(user_id, request.json)
    elif request.method == 'DELETE':
        return UserHandler().deleteUser(user_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/users/<int:user_id>/chats', methods=['GET', 'PUT', 'DELETE'])
def getUserChatList(user_id):
    if request.method == 'GET':
        return UserHandler().getUserChatList(user_id)
    elif request.method == 'PUT':
        return UserHandler().updateUser(user_id, request.json)
    elif request.method == 'DELETE':
        return UserHandler().deleteUser(user_id)
    else:
        return jsonify(Error="Method not allowed."), 405

@app.route('/InstaChat/users/posts/<int:post_id>/<string:react_type>', methods=['GET'])
def getUsersThatReactToPostX(post_id, react_type):
    if request.method == 'GET':
        return UserHandler().getUsersThatReact(post_id, react_type)
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
        return jsonify(Error = "Method not allowed."), 405


@app.route('/InstaChat/posts', methods=['POST', 'GET'])
def getAllPost():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PostHandler().insertPostJson(request.json)
    else:
        if not request.args:
            return PostHandler().getAllPosts()


@app.route('/InstaChat/chats/<int:chat_id>/posts/<int:post_id>', methods=['GET', 'PUT', 'DELETE'])
def getPostById(chat_id, post_id):
    if request.method == 'GET':
        return PostHandler().getPostById(chat_id, post_id)
    elif request.method == 'PUT':
        return PostHandler().updatePost(post_id, request.json)
    elif request.method == 'DELETE':
        return PostHandler().deletePost(post_id)
    else:
        return jsonify(Error = "Method not allowed."), 405

@app.route('/InstaChat/posts/<int:post_id>/reactions', methods=['GET', 'PUT', 'DELETE'])
def getPostReactions(post_id):
    if request.method == 'GET':
        return PostHandler().getPostById(post_id)
    elif request.method == 'PUT':
        return PostHandler().updatePost(post_id, request.json)
    elif request.method == 'DELETE':
        return PostHandler().deletePost(post_id)
    else:
        return jsonify(Error = "Method not allowed."), 405

@app.route('/InstaChat/posts/<int:post_id>/replies', methods=['GET', 'PUT', 'DELETE'])
def getPostReplies(post_id):
    if request.method == 'GET':
        return PostHandler().getPostById(post_id)
    elif request.method == 'PUT':
        return PostHandler().updatePost(post_id, request.json)
    elif request.method == 'DELETE':
        return PostHandler().deletePost(post_id)
    else:
        return jsonify(Error = "Method not allowed."), 405


# @app.route('/InstaChat/sessions', methods=['POST', 'GET'])
# def getAllSessions():
#     if request.method == 'POST':
#         print("REQUEST: ", request.json)
#         return SessionHandler().insertSessionJson(request.json)
#     else:
#         if not request.args:
#             return SessionHandler().getAllSessions()
#
#
# @app.route('/InstaChat/sessions/<int:session_id>', methods=['GET', 'PUT', 'DELETE'])
# def getSessionById(session_id):
#     if request.method == 'GET':
#         return SessionHandler().getSessionById(session_id)
#     elif request.method == 'PUT':
#         return SessionHandler().updateSession(session_id, request.json)
#     elif request.method == 'DELETE':
#         return SessionHandler().deleteSession(session_id)
#     else:
#         return jsonify(Error = "Method not allowed."), 405




if __name__ == '__main__':
    app.run()
