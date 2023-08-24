#!/usr/bin/python3
"""
determines if a given data set
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Return: True if data is a valid
    UTF-8 encoding, else return False
    """
    i = 0
    while i < len(data):
        # Check for single-byte character
        if data[i] <= 127:
            pass  # Valid single-byte character
        # Check for two-byte character
        elif 194 <= data[i] <= 223 and i + 1 < len(data)\
                and 128 <= data[i + 1] <= 191:
            i += 1  # Valid two-byte character
        # Check for three-byte character
        elif 224 <= data[i] <= 239 and i + 2 < len(data) \
                and all(128 <= data[j] <= 191 for j in range(i + 1, i + 3)):
            i += 2  # Valid three-byte character
        # Check for four-byte character
        elif 240 <= data[i] <= 244 and i + 3 < len(data) \
                and all(128 <= data[j] <= 191 for j in range(i + 1, i + 4)):
            i += 3  # Valid four-byte character
        else:
            return False  # Invalid UTF-8 sequence
        i += 1

    return True
