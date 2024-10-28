# https://leetcode.com/problems/longest-repeating-character-replacement/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0

        most_recurring_count = 0
        counts = {}

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            most_recurring_count = max(most_recurring_count, counts[s[r]])

            if (r - left) + 1 - most_recurring_count > k:
                counts[s[left]] -= 1
                left += 1

            max_length = max(max_length, r - left + 1)

        return max_length
