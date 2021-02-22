m = 5
n = 7

def uniquePaths(m: int, n: int) -> int:
    rows = m
    columns = n
    grid = [[1]*columns]*rows #Create grid to count unique paths and start with 1 path
    for row in range(1,rows):
        for column in range(1,columns):
            grid[row][column] = grid[row-1][column] + grid[row][column-1] #Traverse through grid and add previous number of paths to new count
    return grid[-1][-1] #Return final count of unique paths located in last position on grid

print(uniquePaths(m,n))