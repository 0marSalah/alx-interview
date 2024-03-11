#!/usr/bin/python3
""" Island Perimeter """

def island_perimeter(grid):
    """ Given a 2D grid map of 1s (land) and 0s (water), return the perimeter of the island.

    Args:
        grid (List[List[int]]): 2D grid map of 1s (land) and 0s (water)
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Check UP - either it's the first row, or the cell above is water
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                # Check DOWN - either it's the last row, or the cell below is water
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                # Check LEFT - either it's the first column, or the cell to the left is water
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                # Check RIGHT - either it's the last column, or the cell to the right is water
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter
