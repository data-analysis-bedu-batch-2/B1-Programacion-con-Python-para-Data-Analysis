""" Simple REST API with Flask """
import csv
from flask import Flask, jsonify, request

app = Flask(__name__)

def add_user(user_data):
    with open('users.csv', 'a') as csvfile:
        headers=['firstname', 'lastname', 'gender']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writerow(user_data)
    return user_data

def get_users():
    users = []
    with open('users.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users.append(row)
    return users

@app.route('/users', methods=['GET','POST'])
def users_data():
    if request.method == 'POST':
        user_data = request.json
        return jsonify(add_user(user_data)), 201
    else:
        return jsonify(get_users())

if __name__ == "__main__":
    app.run()