#!/usr/bin/env python3
"""
Module Containing __hash_password method
"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """
    Method that hashes password
    """
    bytes = password.encode('utf-8')
    salt = gensalt()
    return hashpw(bytes, salt)
