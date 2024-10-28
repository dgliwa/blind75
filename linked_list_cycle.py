# https://leetcode.com/problems/linked-list-cycle/


from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        node_slow = node_fast = head

        while node_fast.next and node_fast.next.next:
            if node_fast == node_slow:
                return True
            node_slow = node_slow.next  # type: ignore
            node_fast = node_fast.next.next

        return False

    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     nodes = set()
    #
    #     if not head:
    #         return False
    #
    #     node = head
    #
    #     while node:
    #         if node in nodes:
    #             return True
    #
    #         nodes.add(node)
    #         node = node.next
    #
    #     return False
