#!/usr/bin/python3
"""
Module task_04_flask
"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """
    the root URL (“/”)
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    URL "/status"
    """
    return "OK"


@app.route("/data")
def data():
    """
    URL "/data"
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    URL: /users/<username>
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user from request
    """
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
