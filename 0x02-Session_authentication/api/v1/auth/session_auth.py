#!/usr/bin/env python3
"""
Auth module for the Session Auth
"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


class SessionAuth(Auth):
    """
    Child class for Auth
    """
    pass
