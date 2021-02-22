m = 3
n = 7

def uniquePaths(m: int, n: int) -> int:
    rows = m
    columns = n
    grid = [[1]*columns]*rows
    for i in range(1,rows):
        for j in range(1,columns):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[-1][-1]

print(uniquePaths(m,n))