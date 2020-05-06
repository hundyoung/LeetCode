# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from leetcode.Q101_Symmetric_Tree import TreeNode


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        dp=[[[] for _ in range(n+1)] for _ in range(n+1)]
        for l in range(1,n+1):
            for i in range(1,n+1):
                j=l+i
                if j>=n+1:
                    break
                current_result =[]
                for k in range(i,j+1):
                    node = TreeNode(k)
                    current_node_list =[node]
                    if k>i:
                        for m in range(len(dp[i][k])):
                            left_child = dp[i][k][m]
                            node.left=left_child
                    if k<j:
                        for m in range(len(dp[k][j])):
                            pass



