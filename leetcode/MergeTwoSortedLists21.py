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

def printList(listNode:ListNode):
    while listNode!= None:
        print(listNode.val,end="->")
        listNode = listNode.next
    print()
if __name__ == "__main__":
    solution = Solution()
    list1 = []
    list2 = [0]
    if len(list1)>0:
        l1 = ListNode(list1.pop(0))
    else:
        l1 = None
    l1Head = l1
    if len(list2)>0:
        l2 = ListNode(list2.pop(0))
    else:
        l2 = None
    l2Head = l2
    for i in range(len(list1)):
        l1.next = ListNode(list1[i])
        l1 = l1.next
    for i in range(len(list2)):
        l2.next = ListNode(list2[i])
        l2 = l2.next
    printList(l1Head)
    printList(l2Head)
    printList(solution.mergeTwoLists(l1Head,l2Head))