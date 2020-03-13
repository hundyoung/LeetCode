# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return head
        fast_node = head
        slow_node = head
        while fast_node and slow_node:
            slow_node =slow_node.next
            if fast_node.next:
                fast_node = fast_node.next.next
            else:
                return False
            if fast_node==slow_node:
                return True
        return False