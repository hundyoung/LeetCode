# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from leetcode.Q101_Symmetric_Tree import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.deep_level=0
        def bfs(level,node:TreeNode):
            if not node:
                self.deep_level=max(self.deep_level,level)
            else:
                bfs(level+1,node.left)
                bfs(level+1,node.right)
        bfs(1,root)
        return self.deep_level