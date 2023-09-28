#!/usr/bin/python3
"""
function def island_perimeter(grid): that returns
the perimeter of the island described in grid
"""


def is_water(cell):
    """
    Check if a cell is water (0).

    Args:
        cell (int): The value of the cell (0 or 1).

    Returns:
        int: 1 if the cell is water, 0 otherwise.
    """
    return 1 if cell == 0 else 0


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by a grid.

    Args:
        grid (list[list[int]]): A 2D grid where 1 represents land
        and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """

    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Validate grid dimensions
    assert 1 <= rows <= 100 and 1 <= cols <= 100, \
        "Grid dimensions must be between 1 and 100"

    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            assert grid[i][j] in {0, 1}, "Grid values must be 0 or 1"

            if grid[i][j] == 1:
                # Check the four adjacent cells
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
