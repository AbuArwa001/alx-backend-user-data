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
        session_id = uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id
