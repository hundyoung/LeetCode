# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        node = root
        result = []
        x_dict = {}
        def dfs(node,x,y):
            if node:
                y_dict = x_dict.get(x,{})
                y_dict_set=y_dict.get(y,set())
                y_dict_set.add(node.val)
                y_dict[y]=y_dict_set
                x_dict[x]=y_dict
                dfs(node.left,x-1,y-1)
                dfs(node.right,x+1,y-1)
        dfs(node,0,0)
        x_key_sort = sorted(x_dict.items(),key=lambda a:a[0])
        for x,y_dict in x_key_sort:
            y_key_sort = sorted(y_dict.items(), key=lambda a: a[0],reverse=True)
            current_x=[]
            for y,y_dict_set in y_key_sort:
                y_dict_set = sorted(list(y_dict_set))
                for v in y_dict_set:
                    current_x.append(v)
            result.append(current_x)
        return result

a = [3,9,20,None,None,15,7]
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
s = Solution()
print(s.verticalTraversal(root))





