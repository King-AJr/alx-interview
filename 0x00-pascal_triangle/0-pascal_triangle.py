#!/usr/bin/python3
"""A script to determine Pascal's triangle for any number"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle as a list of lists
    for a given number of rows, n.
    """
    pascals_triangle = []

    # If n is less than or equal to 0, return an empty triangle
    if n <= 0:
        return pascals_triangle

    for row in range(n):
        current_row = []

        for position_in_row in range(row + 1):
            # The first and last elements in each row are always 1
            if position_in_row == 0 or position_in_row == row:
                current_row.append(1)
            else:
                # Calculate other elements by adding the two
                # elements from the row above
                previous_row = pascals_triangle[row - 1]
                current_element = previous_row[position_in_row - 1] \
                    + previous_row[position_in_row]
                current_row.append(current_element)

        pascals_triangle.append(current_row)

    return pascals_triangle
