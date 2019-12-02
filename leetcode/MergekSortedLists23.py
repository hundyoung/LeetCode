# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        index1=0
        index2=0
        head = ListNode(float("inf"))
        preNode = head
        while l1!= None and l2!=None:
            if l1.val<l2.val:
                value = l1.val
                l1 = l1.next
            else:
                value = l2.val
                l2 = l2.next
            node = ListNode(value)
            if head.next == None:
                head.next = node
                preNode = node
            else:
                preNode.next = node
                preNode = node
        while l1!=None:
            node = ListNode(l1.val)
            preNode.next = node
            preNode = node
            l1 = l1.next

        while l2!=None:
            node = ListNode(l2.val)
            preNode.next = node
            preNode = node
            l2 = l2.next
        return head.next

    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        while len(lists)>1:
            tempLists = []
            while len(lists) >1:
                tempList1 = lists.pop(0)
                tempList2 = lists.pop(0)
                tempLists.append(self.mergeTwoLists(tempList1,tempList2))

            if len(lists)==1:
                tempLists.append(lists.pop(0))
            lists= tempLists
        if len(lists)==0:
            return None
        return lists.pop(0)

