#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """ Given a 2D grid map of 1s (land) and 0s (water),
    return the perimeter of the island.

    Args:
        grid (List[List[int]]): 2D grid map of 1s (land) and 0s (water)
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
