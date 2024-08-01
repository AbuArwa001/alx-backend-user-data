#!/usr/bin/env python3
"""
Filter logs
"""
import re


def filter_datum(fields, redaction, message, separator):
    """filter_datum that returns the log message obfuscated:"""
    for field in fields:
        message = re.sub(f'{field}=.*?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message
