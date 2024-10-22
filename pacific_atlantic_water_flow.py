# https://leetcode.com/problems/pacific-atlantic-water-flow/

from typing import Deque, List, Set, Tuple
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = deque()
        atlantic = deque()

        for i in range(len(heights)):
            pacific.append((i, 0))
            atlantic.append((i, len(heights[0]) - 1))
        for i in range(len(heights[0])):
            pacific.append((0, i))
            atlantic.append((len(heights) - 1, i))

        can_reach_pacific = self.can_reach(heights, pacific)
        can_reach_atlantic = self.can_reach(heights, atlantic)

        return list(can_reach_pacific.intersection(can_reach_atlantic))  # pyright: ignore

    def can_reach(self, heights: List[List[int]], coastline: Deque[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        reachable_from_coastline = set()

        while coastline:
            tile_y, tile_x = coastline.popleft()
            if (tile_y, tile_x) in reachable_from_coastline:
                continue
            reachable_from_coastline.add((tile_y, tile_x))

            for move in moves:
                y = tile_y + move[0]
                x = tile_x + move[1]
                if y < 0 or y >= len(heights) or x < 0 or x >= len(heights[0]) or heights[y][x] < heights[tile_y][tile_x]:
                    continue
                coastline.append((tile_y, tile_x))

        return reachable_from_coastline
