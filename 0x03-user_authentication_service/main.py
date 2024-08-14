#!/usr/bin/env python3
"""
Main file
"""
import requests


def register_user(email: str, password: str) -> None:
    """
    Register a new user with the given email and password.
    """
    url = "http://localhost:5000/users"
    data = {"email": email, "password": password}

    # Send data as form-encoded
    req = requests.post(url, data=data)
    assert (
        req.status_code == 200
    ), f"Expected status code 200, but got {req.status_code}"
    assert req.json() == {
        "email": email,
        "message": "user created",
    }, f"Unexpected response: {req.json()}"

    # Check for re-registration
    req = requests.post(url, data=data)
    assert (
        req.status_code == 400
    ), f"Expected status code 400, but got {req.status_code}"


def log_in_wrong_password(email: str, password: str) -> None:
    """
    log_in_wrong_password
    a new user with the given email and password.
    """
    url = "http://localhost:5000/sessions"
    data = {"email": email, "password": password}

    # Send data as form-encoded
    req = requests.post(url, data=data)
    assert (
        req.status_code == 401
    ), f"Expected status code 400, but got {req.status_code}"


def log_in(email: str, password: str) -> str:
    """
    log_in USER
    a new user with the given email and password.
    """
    url = "http://localhost:5000/sessions"
    data = {"email": email, "password": password}

    # Send data as form-encoded
    req = requests.post(url, data=data)
    # print(req.json())
    assert (
        req.status_code == 200
    ), f"Expected status code 200, but got {req.status_code}"
    return req.cookies.get("session_id")


def profile_unlogged() -> None:
    """
    profile_unlogged
    a new user with the given email and password.
    """
    url = "http://localhost:5000/profile"
    # Send data as form-encoded
    req = requests.get(url)
    assert (
        req.status_code == 403
    ), f"Expected status code 403, but got {req.status_code}"


def profile_logged(session_id: str) -> None:
    """
    profile_logged
    a new user with the given email and password.
    """
    url = "http://localhost:5000/profile"
    data = str(session_id)
    # Send data as form-encoded
    req = requests.get(url, cookies={"session_id": data})
    assert (
        req.status_code == 200
    ), f"Expected status code 200, but got {req.status_code}"


def log_out(session_id: str) -> None:
    """
    log_out
    a new user with the given email and password.
    """
    url = "http://localhost:5000/sessions"
    req = requests.delete(url, cookies={"session_id": session_id})
    assert (
        req.status_code == 200
    ), f"Expected status code 200, but got {req.status_code}"


def reset_password_token(email: str) -> str:
    """
    reset_password_token
    a new user with the given email and password.
    """
    url = "http://localhost:5000/reset_password"
    data = {"email": email}

    # Send data as form-encoded
    req = requests.post(url, data=data)
    assert (
        req.status_code == 200
    ), f"Expected status code 200, but got {req.status_code}"
    return req.json().get("reset_token")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    update_password
    a new user with the given email and password.
    """
    url = "http://localhost:5000/reset_password"
    data = {
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password,
    }

    # Send data as form-encoded
    req = requests.put(url, data=data)
    assert (
        req.status_code == 200
    ), f"Expected status code 200, but got {req.status_code}"


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
