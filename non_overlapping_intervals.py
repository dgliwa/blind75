# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        
        count = 1
        current = 0
        intervals.sort(key=lambda x: x[1])
        
        for i in range(1, len(intervals)):
            if intervals[current][1] <= intervals[i][0]:
                count += 1
                current = i
        

        
        return len(intervals) - count
        
