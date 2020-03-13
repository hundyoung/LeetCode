class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x+1
        while left<right:
            mid = (left+right+1)>>1
            square = mid*mid
            if square==x:
                left=mid
                break
            elif square<x:
                left=mid
            else:
                right=mid-1
        return left



s = Solution()
print(s.mySqrt(8))