from flask import Flask, jsonify, request
from handlers.chats import ChatHandler


#from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Welcome to the poor mans Instagram!'



@app.route('/InstaChat/chats', methods=['GET', 'POST'])
def getAllParts():
    if request.method == 'POST':
        print("REQUEST: ", request.json)
    else:
        if not request.args:
            return ChatHandler().getAllChats()
        else:
            return

if __name__ == '__main__':
    app.run()
