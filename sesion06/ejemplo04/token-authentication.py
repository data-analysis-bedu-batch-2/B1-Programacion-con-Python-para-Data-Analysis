""" Token authentication """
from flask import Flask, jsonify
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth()

tokens = {
    "secret-token-1": "john",
    "secret-token-2": "jane"
}

@auth.verify_token
def verify_token(token):
    if token in tokens:
        return True
    return False

@app.route('/')
@auth.login_required
def index():
    return jsonify("Hello, world!")

if __name__ == '__main__':
    app.run()