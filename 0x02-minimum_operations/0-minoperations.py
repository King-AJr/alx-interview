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
    """calculates the fewest number of operations
      needed to result in exactly n H characters 
      in the file"""
    i: int = 2
    H: int = 0
    result: int = 0
    if n < 2:
        return 0
    while H < n:
        if H % 2 == 0:
            H = H + i
        else:
            H = H + i + 1
        i += 1
    for j in range(i - 1):
        if j % 2 == 0 and j + 1 % 2 != 0:
            result = result + 1
        else:
            result = result + 2
    return result
