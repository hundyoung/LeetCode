# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head
        # To change
        if head==None:
            return None
        if head.next != None:
            head = head.next

            nextNode = node.next
            nextNextNode = nextNode.next

            node.next = nextNextNode
            nextNode.next = node
            node = nextNextNode
        preNode = head.next

        # printList(head)
        while node != None and node.next != None:
            nextNode = node.next
            nextNextNode = nextNode.next
            node.next = nextNextNode
            nextNode.next = node

            preNode.next = nextNode
            preNode = node

            node = nextNextNode
            # printList(head)
        return head

def printList(listNode:ListNode):
    count=0
    while listNode!= None and count<10:
        print(listNode.val,end="->")
        listNode = listNode.next
        count+=1
    print()
if __name__ == "__main__":
    solution = Solution()
    list1 = [1]
    if len(list1)>0:
        l1 = ListNode(list1.pop(0))
    else:
        l1 = None
    l1Head = l1
    for i in range(len(list1)):
        l1.next = ListNode(list1[i])
        l1 = l1.next
    # printList(l1Head)
    printList(solution.swapPairs(l1Head))
