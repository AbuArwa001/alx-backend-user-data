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
    Return:
      - Current authenticated user objects JSON represented
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    try:
        user = User.search({"email": email})[0]
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if user:
        if user.is_valid_password(password):
            from api.v1.app import auth
            # user
            session_id = auth.create_session(user.id)
            res = jsonify(user.to_json())
            cookie_name = getenv('SESSION_NAME')
            res.set_cookie(cookie_name, session_id)
            return res
        else:
            return jsonify({"error": "wrong password"}), 401
    else:
        return jsonify({"error": "no user found for this email"}), 404


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def logout() -> str:
    """Return:
      - You must use auth.destroy_session(request)
      for deleting the Session ID contains in the reque
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        return False, abort(404)
    else:
        return jsonify({})
