from collections import deque
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]      

class Solution:
    def pacificAtlantic(self, heights):      
        rows, columns = len(heights)-1, len(heights[0])-1
        pacific = deque()
        atlantic = deque()
        
        # Create 2 deques for border cells touching Atlantic and Pacific Oceans
        for column in range(columns+1):
            pacific.append([0, column])
            atlantic.append([rows, column])
        for row in range(rows+1):
            pacific.append([row, 0])
            atlantic.append([row, columns])
        
        # Check for neighbors with water flowing to Pacific
        PacificCells = self.bfs(pacific, columns, rows, heights)

        # Check for neighbors with water flowing to Atlantic
        AtlanticCells = self.bfs(atlantic, columns, rows, heights)
        
        # Finds cells in both sets which flow water to both oceans
        FlowsToBothOceans = PacificCells.intersection(AtlanticCells)
        return FlowsToBothOceans
    
    # Funtion checks neighboring cells to see if they flow water to single ocean
    def bfs(self, Q, columns, rows, heights):
        visited = set()
        for cell in Q:
            visited.add(tuple(cell)) # Adds all border cells to visited (takes care of corner case)
        while Q:
            row, column = Q.popleft()
            directions = ((row+1, column), (row, column+1), (row-1, column), (row, column-1))
            for r,c in directions:
                if 0 <= r <= rows and 0 <= c <= columns:
                    if heights[r][c] >= heights[row][column] and (r,c) not in visited:
                        visited.add((r,c))
                        Q.append([r,c])
        return visited

test = Solution()

print(test.pacificAtlantic(heights))