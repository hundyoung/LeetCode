# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current_node =head
        pre_node = None
        while current_node != None:
            next_node = current_node.next
            current_node.next=pre_node
            pre_node = current_node
            current_node= next_node
        return pre_node

s = Solution()
head = s.reverseList()