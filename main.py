from flask import Flask, jsonify, request


#from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Welcome to the poor mans Instagram!'

if __name__ == '__main__':
    app.run()
