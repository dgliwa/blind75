# https://leetcode.com/problems/merge-intervals/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            curr_interval = merged_intervals[-1]
            interval_to_merge = intervals[i]

            if curr_interval[1] >= interval_to_merge[0]:
                if curr_interval[1] <= interval_to_merge[1]:
                    curr_interval[1] = interval_to_merge[1]
            else:
                merged_intervals.append(interval_to_merge)

        return merged_intervals
