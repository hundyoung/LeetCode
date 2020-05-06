# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from leetcode.Q101_Symmetric_Tree import TreeNode

import copy
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        def dfs(l,r):
            if l>r:
                return [None]
            else:
                node_list=[]
                for i in range(l,r+1):
                    left_Nodes = dfs(l,i-1)
                    right_Nodes = dfs(i+1,r)
                    for l_c in left_Nodes:
                        for r_c in right_Nodes:
                            node = TreeNode(i)
                            node.left=l_c
                            node.right=r_c
                            node_list.append(node)
                return node_list
        return dfs(1,n)
s = Solution()
print(s.generateTrees(3))




