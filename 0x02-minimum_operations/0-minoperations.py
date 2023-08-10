#!/usr/bin/python3


"""
In a text file, there is a single
character H. Your text editor can execute
only two operations in this file: Copy All
and Paste
Given a minOperations(n)
calculates the fewest number of
operations needed to result in
exactly n H characters in
the file.
"""


def minOperations(n: int) -> int:
    """calculates the fewest number of operations
      needed to result in exactly n H characters
      in the file"""
    prev: str = 'H'
    body: str = 'H'
    index: int = 0
    while (len(body) < n):
        if n % len(body) == 0:
            index += 2
            prev = body
            body += body
        else:
            index += 1
            body += prev
    if len(body) != n:
        return 0
    return index
