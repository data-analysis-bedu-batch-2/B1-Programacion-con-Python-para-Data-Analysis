""" Hello world with Flask """
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return f'Hello, World!'

if __name__ == "__main__":
    app.run()