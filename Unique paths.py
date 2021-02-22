m = 3
n = 7

def uniquePaths(m: int, n: int) -> int:
    rows = m
    columns = n
    grid = [[1]*columns]*rows
    for row in range(1,rows):
        for column in range(1,columns):
            grid[row][column] = grid[row-1][column] + grid[row][column-1]
    return grid[-1][-1]

print(uniquePaths(m,n))