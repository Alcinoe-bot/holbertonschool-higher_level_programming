#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required
from flask_jwt_extended import get_jwt, JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'your_super_secret_key'
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Check user credentials for Basic Auth.
    """
    if username in users and check_password_hash(
       users[username]["password"], password):
        return username
    return None


@app.route('/login', methods=["POST"])
def user_login():
    """
    Verify user and return JWT if valid.
    """
    username = request.json.get("username")
    password = request.json.get("password")
    log = verify_password(username, password)

    if log is None:
        return jsonify({"error": "invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]})
    return jsonify(access_token=access_token)


@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def auth_basic():
    """
    Route protected with Basic Auth.
    """
    return "Basic Auth: Access Granted"


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Route protected with JWT.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Grant access only if user is admin.
    """
    identity = get_jwt()
    user_role = identity.get("role")
    if user_role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Respond to missing JWT.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Respond to bad JWT format.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Respond to expired JWT.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Respond to revoked JWT.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Respond to missing fresh JWT.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
