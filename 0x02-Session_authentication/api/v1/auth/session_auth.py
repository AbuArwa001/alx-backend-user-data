#!/usr/bin/env python3
"""
Auth module for the Session Auth
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar
from uuid import uuid4


class SessionAuth(Auth):
    """
    Child class for Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id:
        Return:
            None if user_id is None
            None if user_id is not a string
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        # print(self.user_id_by_session_id)
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        (overload) that returns a
        User instance based on a cookie value:
        """
        cookie = self.session_cookie(request)

        if cookie:
            user_id = self.user_id_for_session_id(cookie)
            print(self.user_id_by_session_id)
            if user_id:
                user = User.get(user_id)
                return user

    def destroy_session(self, request=None):
        """
        Method that deletes the user session / logout:
        """
        if request is None:
            return False
        cookie = self.session_cookie(request)
        if not cookie:
            return False
        session_id = self.user_id_for_session_id(cookie)
        if not session_id:
            return False
        print(session_id)

        self.user_id_by_session_id.pop(cookie, None)
        # del self.user_id_by_session_id[cookie]
        return True
