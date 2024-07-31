#!/usr/bin/env python3
"""
FIlter logs
"""
import re
from typing import Callable


def filter_datum(fields, redaction, message, separator):
    """
    Function to find and replace comas
    """
    # Build the regex pattern dynamically
    regex_parts = []
    for field in fields:
        if field == "date_of_birth":
            regex_parts.append(f"({field})=\\d{{2}}/\\d{{2}}/\\d{{4}}")
        else:
            regex_parts.append(f"({field})=[^;]+")
    regex = f"{separator}".join(regex_parts)

    # Function to replace the matched groups
    def replace_values(match: Callable) -> str:
        """
        Helper function for sub
        """
        replacements = []
        lst = match.groups()
        match_g = len(match.groups())
        for i in range(1,  match_g + 1):
            field_name = match.group(i)
            replacements.append(f"{field_name}={redaction}")
        # if i > 1:
        #     return f"{separator}".join(replacements) + separator
        # else:
        return f"{separator}".join(replacements)

    # Substitute the values using the replace_values function
    result = re.sub(regex, replace_values, message)
    return result
