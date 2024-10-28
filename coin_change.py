# https://leetcode.com/problems/coin-change/

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        combinations = [amount + 1] * (amount + 1)
        combinations[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    combinations[i] = min(combinations[i - c] + 1, combinations[i])

        return combinations[amount] if combinations[amount] < amount + 1 else -1

        
        

