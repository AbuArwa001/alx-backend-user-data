#!/usr/bin/env python3
"""
Module Auth for the API
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Class Auth for the API
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        # return f"{False} - {path} "
        return False

    def authorization_header(self, request=None) -> str:
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        return None