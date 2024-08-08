#!/usr/bin/env python3
"""
Module Auth for the API
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """
    Class Auth for the API
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if path require auth
        """
        if not path or not excluded_paths:
            return True
        if not path.endswith('/'):
            path = path + '/'
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path.rstrip('*')):
                    return False
            elif path == excluded_path:
                return False
        # if path in excluded_paths:
        #     return False
        # else:
        return True

    def authorization_header(self, request=None) -> str:
        """
        Check for Authorizationn Header and returns it
        """
        # print("AUTH HEADERS",request.headers)
        if not request or 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Check if the current user
        """
        return None

    def session_cookie(self, request=None):
        if request is None:
            return None
        name = getenv('SESSION_NAME')
        return request.cookies.get(name)
