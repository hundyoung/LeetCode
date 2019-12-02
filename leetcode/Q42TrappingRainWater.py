from typing import List



class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==0:
            return 0
        areaList = [0 for i in range(len(height))]
        leftTopIndex = 0
        preStart = 0
        for i in range(1,len(height)):
            if height[i]>height[i-1]:
                for j in range(i-1,leftTopIndex-1,-1):
                    if j==leftTopIndex or height[j]>= height[i]:
                        width = i-j-1
                        h = min(height[i],height[j])
                        area = h * width
                        for k in range(j+1,i):
                            area -= height[k]
                        currentTotalArea = area + areaList[j]
                        areaList[i] = currentTotalArea
                        break
                if height[i]>=height[leftTopIndex]:
                    leftTopIndex = i
            else:
                areaList[i] = areaList[i-1]
        return areaList[-1]
s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))