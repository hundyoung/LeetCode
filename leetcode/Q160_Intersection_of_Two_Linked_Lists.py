# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        c_a = headA
        c_b = headB
        while c_a!=c_b:
            if c_a:
                c_a=c_a.next
            else:
                c_a=headB
            if c_b:
                c_b=c_b.next
            else:
                c_b=headA
        return c_a