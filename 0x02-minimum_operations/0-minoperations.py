#!/usr/bin/python3
"""
In a text file, there is a single
character H. Your text editor can execute
only two operations in this file: Copy All
and Paste
Given a minOperations(n) calculates
the fewest number of operations needed
to result in exactly n H characters in
the file.
"""

def minOperations(n: int) -> int:
    """calculates
    the fewest number of operations needed
    to result in exactly n H characters in
    the file."""
    i: int = 2
    result: int = 0
    if n < 2:
        return 0
    while result < n:
        if i % 2 == 0:
            result = result + (i - 1)
        else:
            result = result + i
        i += 1
    add: int = n / 10
    if add > 1:
        i += add
    return int(i)
