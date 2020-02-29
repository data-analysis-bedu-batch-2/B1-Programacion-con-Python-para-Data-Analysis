""" Simple REST API with Flask """
from flask import Flask, jsonify, request

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
    {
        "firstname": "Mike",
        "lastname": "Doe",
        "gender": "M"
    },
]

def get_filtered_data(field, value):
    filtered_data = filter(lambda x: x[field] == value, data)
    return list(filtered_data)

@app.route('/users')
def users_data():
    gender = request.args.get('gender')
    if gender:
        return jsonify(
            get_filtered_data('gender', gender)
        )
    return jsonify(data)

if __name__ == "__main__":
    app.run()