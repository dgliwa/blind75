# https://leetcode.com/problems/number-of-islands/

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        island_count = 0

        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    island_count += 1
                    bfs = deque([(i, j)])

                    while bfs:
                        x, y = bfs.pop()
                        grid[x][y] = "0"

                        for move in moves:
                            new_x = x + move[0]
                            new_y = y + move[1]

                            if new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[new_x]) and grid[new_x][new_y] == "1":
                                bfs.append((new_x, new_y))
        return island_count
