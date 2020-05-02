# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode.Q987_Vertical_Order_Traversal_of_a_Binary_Tree import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def bsf(node:TreeNode,min_val,max_val):
            if node:
                val = node.val
                if val <= min_val or val >= max_val:
                    return False
                if not bsf(node.left,min_val,val):
                    return False
                if not bsf(node.right,val,max_val):
                    return False
                return True
            else:
                return True
        return bsf(root,float('-inf'),float('inf'))
a = [1,1]
def treeDfs(node,i):
    if i*2+2<len(a):
        if a[i*2+1]:
            left = TreeNode(a[i*2+1])
            node.left=left
            treeDfs(left,i*2+1)
        if a[i*2+2]:
            right = TreeNode(a[i*2+2])
            node.right = right
            treeDfs(right,i*2+2)
root = TreeNode(a[0])
treeDfs(root,0)
s =Solution()
print(s.isValidBST(root))