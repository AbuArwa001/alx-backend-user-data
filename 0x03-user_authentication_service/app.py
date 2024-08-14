#!/usr/bin/env python3
"""
Simple flask APP
"""
from flask import (
    Flask,
    jsonify,
    request,
    abort,
    redirect,
    url_for,
    make_response,
)
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    """
    Index route
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"])
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


@app.route("/sessions", methods=["POST"])
def login() -> str:
    """
    Login User route
    """
    email: str = request.form.get("email")
    password: str = request.form.get("password")
    user = Auth.valid_login(AUTH, email, password)
    if not user:
        abort(401)
    else:
        session_id = AUTH.create_session(email)
        resp = make_response({"email": email, "message": "logged in"})
        resp.set_cookie("session_id", session_id)
        return resp


@app.route("/sessions", methods=["DELETE"])
def logout() -> str:
    """
    Logout User route
    """
    session_id: str = request.form.get("session_id") or request.cookies.get(
        "session_id"
    )
    user = Auth.get_user_from_session_id(AUTH, session_id)
    if user is None:
        abort(403)
    else:
        AUTH.destroy_session(user.id)
        return redirect(url_for("index"))


@app.route("/profile", methods=["GET"])
def profile():
    """
    function to respond to the GET /profile route.
    The request is expected to contain a session_id cookie
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.id}), 200
    else:
        abort(403)


@app.route("/reset_password", methods=["POST"])
def get_reset_password_token() -> str:
    """
    function to respond to the POST
    /reset_password route
    """
    email = request.form.get("email")
    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "reset_token": token}), 200


@app.route("/reset_password", methods=["PUT"])
def update_password() -> str:
    """
    function in the app module to respond to
    the PUT /reset_password route.
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
