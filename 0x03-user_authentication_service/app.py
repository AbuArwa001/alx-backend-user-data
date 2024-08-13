#!/usr/bin/env python3
"""
Simple flask APP
"""
from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    Index route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users() -> str:
    """
    Add User route
    """
    email: str = request.form.get("email")
    password: str = request.form.get("password")
    try:
        user = Auth.register_user(AUTH, email, password)
    except ValueError as e:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": user.email, "message": "user created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
