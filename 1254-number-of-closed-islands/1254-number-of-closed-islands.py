class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            stack = [[i,j]]
            closed = True
            while stack:
                i,j = stack.pop()
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 0:
                    if i == 0 or j == 0 or i == m-1 or j == n-1:
                        closed = False
                    stack += [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
                    grid[i][j] = 1
            return closed

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                closed = dfs(grid, i, j)
                if closed:
                    cnt += 1

        return cnt

        