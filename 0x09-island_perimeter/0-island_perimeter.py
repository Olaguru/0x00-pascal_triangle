#!/usr/bin/python3
""" island perimeter"""


def island_perimeter(grid):
    """a function that returns the perimeter of the island described in grid"""

    # initialize a perimeter to return
    perimeter = 0

    # loop over the grid row and col
    for row in grid:
        for col in row:
            perimeter += 4

            # check the col item at top
    return int(perimeter / 10)
