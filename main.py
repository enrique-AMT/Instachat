from flask import Flask, jsonify, request
from handlers.chats import ChatHandler
from handlers.posts import PostHandler
from handlers.image import ImagesHandler
from handlers.users import UserHandler
from handlers.reply import ReplyHandler
from handlers.reacts import ReactHandler
from handlers.hashtags import HashtagsHandler
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/')
def greeting():
    return 'Welcome to InstaChat!'

# ========================================= CHAT OPERATIONS ============================================= #


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


@app.route('/InstaChat/chats/<int:chat_id>/owner', methods=['GET'])
def getChatOwner(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatOwner(chat_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/chats/<int:chat_id>', methods=['GET', 'PUT', 'DELETE'])
def getChatById(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatById(chat_id)
    elif request.method == 'PUT':
        return ChatHandler().updateChat(chat_id, request.json)
    elif request.method == 'DELETE':
        return ChatHandler().deleteChat(chat_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/chats/<int:chat_id>/posts', methods=['GET', 'PUT', 'DELETE'])
def getChatPosts(chat_id):
    if request.method == 'GET':
        return PostHandler().getChatPosts(chat_id)
    elif request.method == 'PUT':
        return ChatHandler().updateChat(chat_id, request.json)
    elif request.method == 'DELETE':
        return ChatHandler().deleteChat(chat_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/chats/<int:chat_id>/users', methods=['GET', 'PUT', 'DELETE', 'POST'])
def getChatUsers(chat_id):
    if request.method == 'GET':
        return ChatHandler().getChatUsers(chat_id)
    elif request.method == 'PUT':
        return ChatHandler().updateChat(chat_id, request.json)
    elif request.method == 'DELETE':
        return ChatHandler().deleteChat(chat_id)
    else:
        return jsonify(Error="Method not allowed."), 405


# ========================================= USER OPERATIONS ============================================= #


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


@app.route('/InstaChat/users/<string:username>', methods=['GET', 'PUT', 'DELETE'])
def getUserByUsername(username):
    if request.method == 'GET':
        return UserHandler().getUserByUsername(username)
    elif request.method == 'PUT':
        return UserHandler().updateUser(username, request.json)
    elif request.method == 'DELETE':
        return UserHandler().deleteUser(username)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/users/<int:user_id>/contacts', methods=['GET', 'PUT', 'DELETE'])
def getUserContactList(user_id):
    if request.method == 'GET':
        return UserHandler().getUserContactList(user_id)
    elif request.method == 'PUT':
        return UserHandler().updateUser(user_id, request.json)
    elif request.method == 'DELETE':
        return UserHandler().removeUserFromContacts(user_id)
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


# ========================================= DASHBOARD OPERATIONS ============================================== #


@app.route('/InstaChat/dashboard/hashtags', methods=['GET', 'POST'])
def getDailyHashtags():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().createChat(request.json)
    else:
        if not request.args:
            return HashtagsHandler().getDailyHashtags()
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

@app.route('/InstaChat/dashboard/likes', methods=['GET', 'POST'])
def getDailyLikes():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().createChat(request.json)
    else:
        if not request.args:
            return ReactHandler().getDailyLikes()
        else:
            return

@app.route('/InstaChat/dashboard/dislikes', methods=['GET', 'POST'])
def getDailyDislikes():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().createChat(request.json)
    else:
        if not request.args:
            return ReactHandler().getDailyDislikes()
        else:
            return

@app.route('/InstaChat/dashboard/users', methods=['GET', 'POST'])
def getActiveUsers():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().createChat(request.json)
    else:
        if not request.args:
            return UserHandler().getActiveUsers()
        else:
            return

@app.route('/InstaChat/dashboard/users/<int:user_id>', methods=['GET', 'POST'])
def getDailyPostsForUser(user_id):
    if request.method == 'GET':
        print("REQUEST: ", request.json)
        return PostHandler().getDailyPostsForUser(user_id)
    else:
        if not request.args:
            print("not implemented.")
        else:
            return
@app.route('/InstaChat/dashboard/replies', methods=['GET', 'POST'])
def getDailyReplies():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ChatHandler().createChat(request.json)
    else:
        if not request.args:
            return ReplyHandler().getDailyReplies()
        else:
            return


# ========================================= REACT OPERATIONS ============================================= #


@app.route('/InstaChat/reacts', methods=['POST', 'GET'])
def getAllReacts():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ReactHandler().insertReact(request.json)
    else:
        if not request.args:
            return ReactHandler().getAllReacts()


@app.route('/InstaChat/reacts/<int:react_id>', methods=['GET'])
def getReactById(react_id):
    if request.method == 'GET':
        return ReactHandler().getReactById(react_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/posts/<int:post_id>/reacts/<string:react_type>', methods=['GET'])
def getReactsOnPost(post_id, react_type):
    if request.method == 'GET':
        return ReactHandler().getReactsOnPost(post_id, react_type)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/replies/<int:reply_id>/reacts/<string:react_type>', methods=['GET'])
def getReactsOnReplies(reply_id, react_type):
    if request.method == 'GET':
        return ReactHandler().getReactsOnReplies(reply_id, react_type)
    else:
        return jsonify(Error="Method not allowed."), 405


# ========================================= REPLY OPERATIONS ============================================= #


@app.route('/InstaChat/replies', methods=['POST', 'GET'])
def getAllReplies():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return ReplyHandler().insertReply(request.json)
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


# ========================================= POST OPERATIONS ============================================= #


@app.route('/InstaChat/posts', methods=['POST', 'GET'])
def getAllPost():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
        return PostHandler().insertPost(request.json)
    else:
        if not request.args:
            return PostHandler().getAllPosts()


@app.route('/InstaChat/chats/<int:chat_id>/posts/<int:post_id>', methods=['GET', 'PUT', 'DELETE'])
def getPostsInChatX(chat_id, post_id):
    if request.method == 'GET':
        return PostHandler().getPostsInChatX(chat_id, post_id)
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
        return ReplyHandler().getPostReplies(post_id)
    elif request.method == 'PUT':
        return PostHandler().updatePost(post_id, request.json)
    elif request.method == 'DELETE':
        return PostHandler().deletePost(post_id)
    else:
        return jsonify(Error = "Method not allowed."), 405


# ======================================== REMOVE/INSERT OPERATIONS ============================================ #


@app.route('/InstaChat/chats/<int:chat_id>/users/<int:user_id>', methods=['POST', 'DELETE'])
def removeInsertUserFromToChat(chat_id, user_id):
    if request.method == 'POST':
        return ChatHandler().insertUserToChat(chat_id, user_id)
    elif request.method == 'DELETE':
        return UserHandler().removeUserFromChat(user_id, chat_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/users/<int:user_id>/contacts/<int:contact_id>', methods=['DELETE', 'POST'])
def removeInsertUserFromContactList(user_id, contact_id):
    if request.method == 'DELETE':
        return UserHandler().removeUserFromContacts(user_id, contact_id)
    elif request.method == 'POST':
        return UserHandler().insertUserToContacts(user_id, contact_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/chats/<int:chat_id>/owner/<int:owner_id>', methods=['DELETE'])
def removeChat(chat_id, owner_id):
    if request.method == 'DELETE':
        return ChatHandler().removeChat(chat_id, owner_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/hashtags', methods=['POST', 'GET'])
def hashtag():
    if request.method == 'POST':
        return HashtagsHandler().createHashtag(request.json)
    elif request.method == 'GET':
        return HashtagsHandler().getAllHashtags()
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/posts/<int:post_id>/hashtags', methods=['POST', 'GET'])
def hashtagToPost(post_id):
    if request.method == 'POST':
        return HashtagsHandler().insertHashtagToPost(request.json)
    elif request.method == 'GET':
        return HashtagsHandler().getHashtagsPostX(post_id)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/InstaChat/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return UserHandler().login(request.json)
    else:
        return jsonify(Error="Method not allowed."), 405
@app.route('/InstaChat/image', methods=['POST'])
def postImage():
  if request.method == 'POST':
    return ImagesHandler().insertImage(request.json)


if __name__ == '__main__':
    app.run()
