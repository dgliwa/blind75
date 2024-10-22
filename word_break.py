# https://leetcode.com/problems/word-break/?envType=problem-list-v2&envId=oizxjoit

from typing import List


class Solution:
    def wordBreakFail(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        string = ""
        for i, c in enumerate(s):
            string += c
            if string in words:
                return self.wordBreak(s[i+1:], wordDict)
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)

        if s in wordDict:
            return True

        arr = [True] + [False] * n

        for i in range(1, n + 1):
            for j in range(i):

                if arr[j] and s[j:i] in words:
                    arr[i] = True
                    break

        return arr[-1]


"""
leetcode

n = 8
arr = [True, False, False, False, False, False, False, False, False]

leet # i = 4, j = 0


"""
