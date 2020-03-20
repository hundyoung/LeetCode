# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        def back_tack(left_node:TreeNode,right_node:TreeNode):
            if left_node and right_node:
                if left_node.val == right_node.val:
                    result = back_tack(left_node.left,right_node.right) and back_tack(left_node.right,right_node.left)
                else:
                    result = False
            else:
                if left_node or right_node:
                    result = False
                else:
                    result = True
            return result
        result = back_tack(root.left,root.right)

        return result

