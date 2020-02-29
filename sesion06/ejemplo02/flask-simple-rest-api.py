""" Simple REST API with Flask """
from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {
        "firstname": "Jhon",
        "lastname": "Doe",
        "gender": "M"
    },
    {
        "firstname": "Jane",
        "lastname": "Doe",
        "gender": "F"
    },
]

@app.route('/users')
def users_data():
    return jsonify(data)

@app.route('/users/<int:id>')
def user_data(id):
    try:
        return jsonify(data[id - 1])
    except IndexError:
        return jsonify({'message': 'User not found'}), 404

if __name__ == "__main__":
    app.run()