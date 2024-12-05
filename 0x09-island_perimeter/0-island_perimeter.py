#!/usr/bin/python3
""" island perimeter"""


def island_perimeter(grid):
    """a function that returns the perimeter of the island described in grid"""

    # initialize a perimeter to return
    perimeter = 0

    # loop over the grid row and col
    for row in range(len(grid)):
        for col in range(len(grid[row])):

            # only when we see 1 should we add 4
            if grid[row][col] == 1:
                perimeter += 4

                # check the item at top
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1

                # check the item below
                if row < len(grid) - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1

                # checkn the item left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1

                # check the item right
                if col < len(grid[row]) - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1

    return perimeter
