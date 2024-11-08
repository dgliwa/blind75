# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lower = p if p.val < q.val else q
        higher = p if p.val > q.val else q
        
        node = root

        while node:
            if lower.val <= node.val and higher.val >=node.val:
                return node
            elif lower.val > node.val:
                node = node.right
            else:
                node = node.left
        return root
        
