class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        m ,n  = len(grid), len(grid[0])
        def bfs(grid, i, j):
            deque = [[i, j]]
            while deque:
                i, j = deque.pop()
                if 0 <= i < m and 0 <= j < n and grid[i][j] == "1":
                    deque += [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
                    grid[i][j] = "0" 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    continue
                bfs(grid, i, j)
                cnt += 1
        return cnt
        