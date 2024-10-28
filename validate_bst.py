# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional, Tuple, Deque
from collections import deque

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        nodes: Deque[Tuple[Optional[TreeNode], int | None, int | None]] = deque([
                                                                               (root, None, None)])

        while nodes:
            node, min_val, max_val = nodes.pop()
            if not node:
                continue

            if (min_val is not None and node.val <= min_val) or (max_val is not None and node.val >= max_val):
                return False

            if node.left:
                nodes.append((node.left, min_val, node.val))
            if node.right:
                nodes.append((node.right, node.val, max_val))

        return True
