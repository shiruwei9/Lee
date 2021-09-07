class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        def dfs(x,y):
            if not(0 <= x < len(grid) and 0 <= y < len(grid[0])):
                return 0
            if grid[x][y] == 0:
                return 0    
            if grid[x][y] == 1:
                grid[x][y] = 0
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                return (1 + dfs(x+1,y) + dfs(x-1,y) + dfs(x,y+1) + dfs(x,y-1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxarea = max(maxarea,dfs(i,j))
        return maxarea
                