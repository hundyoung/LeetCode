# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return True
        elif not root.left or not root.right:
            return False
        else:
            pass
