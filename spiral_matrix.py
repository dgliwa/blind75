# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = c = 0
        dir = "R"
        res = []

        num_of_remaining_tiles = len(matrix) * len(matrix[0])

        while num_of_remaining_tiles > 0:
            res.append(matrix[r][c])
            matrix[r][c] = "x"  # type: ignore

            if dir == "R":
                if c + 1 >= len(matrix[r]) or matrix[r][c + 1] == "x":
                    dir = "D"
                    r += 1
                else:
                    c += 1

            elif dir == "D":
                if r + 1 >= len(matrix) or matrix[r + 1][c] == "x":
                    dir = "L"
                    c -= 1
                else:
                    r += 1

            elif dir == "L":
                if c - 1 < 0 or matrix[r][c - 1] == "x":
                    dir = "U"
                    r -= 1
                else:
                    c -= 1
            elif dir == "U":
                if r - 1 < 0 or matrix[r - 1][c] == "x":
                    dir = "R"
                    c += 1
                else:
                    r -= 1
            num_of_remaining_tiles -= 1

        return res
