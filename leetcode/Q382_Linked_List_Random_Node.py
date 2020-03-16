# Definition for singly-linked list.
import random
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.length_count = 1
        self.head = head
        c_node = head
        while c_node.next:
            self.length_count+=1
            c_node=c_node.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        r = random.randrange(self.length_count)
        # r = random.randint(0,self.length_count)
        # count = 0
        c_node = self.head
        for i in range(r):
            c_node = c_node.next
            # count+=1
        return c_node.val
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()