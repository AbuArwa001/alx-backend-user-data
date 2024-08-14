#!/usr/bin/env python3
"""
Module Containing __hash_password method
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from bcrypt import hashpw, gensalt, checkpw
from uuid import uuid4
from typing import Union


def _hash_password(password: str) -> bytes:
    """
    Method that hashes password
    """
    bytes = password.encode("utf-8")
    salt = gensalt()
    return hashpw(bytes, salt)


def _generate_uuid() -> str:
    """
    The function should
    return a string representation of a new UUID.
    """
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Takes mandatory email and
        password string arguments and return a User object.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                raise ValueError(f"User {user.email} already exists")
        except NoResultFound as nf:
            hashed_pwd = _hash_password(password)
            user = self._db.add_user(email, hashed_pwd)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        It should expect email and
        password required arguments and return a boolean.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        hashed = password.encode("utf-8")
        # hashed = _hash_password(password)
        if checkpw(hashed, user.hashed_password):
            return True
        return False

    def create_session(self, email: str) -> str:
        """
        create_session method. It takes an email
        string argument and returns the session ID as a string.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
        except NoResultFound:
            return False
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """
        It takes a
        single session_id string argument
        and returns the corresponding User or None.
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id) -> None:
        """
        The method takes a single user_id integer
        argument and returns None.
        """
        self._db.update_user(user_id, session_id=None)
        return None

    def get_reset_password_token(self, email: str) -> str:
        """
        It takes an
        email string argument and returns a string.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError()
        except InvalidRequestError:
            raise ValueError()
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        It takes reset_token string
        argument and a password string argument and returns None
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except (NoResultFound, InvalidRequestError):
            raise ValueError()
        hashed_pwd = _hash_password(password)
        self._db.update_user(
            user.id, hashed_password=hashed_pwd, reset_token=None
        )
