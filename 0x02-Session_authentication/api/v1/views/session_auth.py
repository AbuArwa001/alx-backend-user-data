#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
from os import getenv

@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /auth_session/login
    Handles user login and session creation
    Return:
      - JSON representation of the current authenticated user object
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    # Search for the user by email
    users = User.search({"email": email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]

    # Check if the provided password is valid
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Create a session for the user
    session_id = auth.create_session(user.id)
    if not session_id:
        return jsonify({"error": "could not create session"}), 500

    # Prepare the response with user data and set the session cookie
    res = jsonify(user.to_json())
    cookie_name = getenv('SESSION_NAME', 'session_id')
    res.set_cookie(cookie_name, session_id)

    return res
