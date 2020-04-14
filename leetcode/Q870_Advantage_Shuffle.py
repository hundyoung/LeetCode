from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        def binarySearch(n_list,target):
            left = 0
            right = len(n_list)
            while left<right:
                mid = (left+right)>>1
                if n_list[mid]<=target:
                    left=mid+1
                else:
                    right=mid
            return left
        A = sorted(A)
        result = []
        for i in range(len(B)):
            n_b = B[i]
            j = binarySearch(A,n_b)
            if j==len(A):
                result.append(A.pop(0))
            else:
                result.append(A.pop(j))
        return result
s = Solution()
A,B = [2,7,11,15],[1,10,4,11]
print(s.advantageCount(A,B))

