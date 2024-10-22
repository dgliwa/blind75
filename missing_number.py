# https://leetcode.com/problems/missing-number/

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        total = 0
        for i in range(1, n + 1):
            total += i

        for num in nums:
            total -= num
        return total
