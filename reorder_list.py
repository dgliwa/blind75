# https://leetcode.com/problems/reorder-list/

from typing import Optional

from collections import deque

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        nodes = deque()
        node = head.next

        while node:
            nodes.append(node)
            node = node.next

        node = head
        while nodes:
            last = nodes.pop()
            node.next = last
            node = last

            if nodes:
                first = nodes.popleft()
                node.next = first
                node = first
            node.next = None
