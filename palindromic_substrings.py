# https://leetcode.com/problems/palindromic-substrings/description/

from collections import deque

class Solution:
    def countSubstrings(self, s: str) -> int:
        valid_palindromes = deque([(i, i + 1) for i in range(len(s))])

        count = 0

        palindromes = set()
        while valid_palindromes:
            p = valid_palindromes.pop()

            if (p[0], p[1]) in palindromes:
                continue

            substr = s[p[0]:p[1]]
            if substr == substr[::-1]:
                palindromes.add((p[0], p[1]))
                count += 1
                if p[0] >= 0 or p[1] <= len(s):
                    new_p0 = max(p[0] - 1, 0)
                    new_p1 = min(len(s), p[1] + 1)

                    if (new_p0, new_p1) not in palindromes:
                        valid_palindromes.append((new_p0, new_p1))
                        
                    new_p0 = max(p[0], 0)
                    new_p1 = min(len(s), p[1] + 1)

                    if (new_p0, new_p1) not in palindromes:
                        valid_palindromes.append((new_p0, new_p1))
            
                    new_p0 = max(p[0] - 1, 0)
                    new_p1 = min(len(s), p[1])

                    if (new_p0, new_p1) not in palindromes:
                        valid_palindromes.append((new_p0, new_p1))
        return count
        
