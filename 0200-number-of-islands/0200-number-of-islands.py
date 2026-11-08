class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        cnt = 0
        m ,n  = len(grid), len(grid[0])
        def dfs(grid, i, j):
            stack = [[i, j]]
            while stack:
                i, j = stack.pop()
                if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                    stack += [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
                    grid[i][j] = "0" 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                dfs(grid, i, j)
                cnt += 1
        return cnt
        