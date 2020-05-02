# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from leetcode.MergeTwoSortedLists21 import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        root= ListNode()
        pre_node=root
        while l1 and l2:
            if l1 and l1.val<l2.val:
                next_node = l1.next
                pre_node.next=l1
                pre_node=l1
                l1=next_node
            else:
                next_node = l2.next
                pre_node.next=l2
                pre_node=l2
                l2=next_node
        pre_node.next=l1 if not l1 else l2
        return root.next