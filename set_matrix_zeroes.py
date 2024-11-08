# https://leetcode.com/problems/set-matrix-zeroes/


from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for k in range(len(matrix)):
                        if k != i and matrix[k][j] != 0:
                            matrix[k][j] = "*" # type: ignore
                    for k in range(len(matrix[0])):
                        if k != j and matrix[i][k] != 0:
                            matrix[i][k] = "*" # type: ignore
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "*":
                    matrix[i][j] = 0
