from flask import Flask, jsonify, request
from handlers.chats import ChatHandler
from handlers.users import UserHandler
from handlers.reply import ReplyHandler


#from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Welcome to the poor mans Instagram!'



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
        return ReplyHandler.getReplyById(reply_id)
    else:
        return jsonify(Error="Method not allowed."), 405

if __name__ == '__main__':
    app.run()
