from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        islandNumber = 0

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    islandNumber += 1
                    dfs(i, j)

        return islandNumber
