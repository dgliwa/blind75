# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        if nums[start] < nums[end] or start == end:
            return nums[0]

        while start < end:
            midpoint = (start + end) // 2
            if nums[midpoint] > nums[end]:
                start = midpoint + 1
            else:
                end = midpoint
        return nums[start]

