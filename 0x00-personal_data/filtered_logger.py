#!/usr/bin/env python3
"""
Filter logs
"""
import re
from typing import Callable


def filter_dec(func: Callable) -> Callable:
    """
    Filter decorator
    """
    def wrapper(fields, redaction, message, separator):
        def replace_values(match):
            """
            Replace values
            """
            replacements = [f"{match.group(i)}={redaction}"
                            for i in range(1, len(match.groups()) + 1)]
            return separator.join(replacements)

        # Build the regex pattern dynamically
        regex_parts = []
        for field in fields:
            if field == "date_of_birth":
                regex_parts.append(f"({field})=\\d{{2}}/\\d{{2}}/\\d{{4}}")
            else:
                regex_parts.append(f"({field})=[^;]+")
        regex = separator.join(regex_parts)

        return re.sub(regex, replace_values, message)

    return wrapper


@filter_dec
def filter_datum(fields, redaction, message, separator):
    """
    filter_datum that returns the log message obfuscated:
    """
    pass
