class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            stack = [[i, j]]
            area = 0
            while stack:
                i, j = stack.pop()
                if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                    stack += [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
                    grid[i][j] = 0
                    area += 1
            return area

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                max_area = max(dfs(grid, i, j), max_area)

        return max_area

        