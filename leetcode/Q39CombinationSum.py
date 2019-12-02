from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        digDict = {}
        minDig = float("inf")
        for i in range(len(candidates)):
            digDict[candidates[i]]=candidates[i]
            minDig= min(minDig,candidates[i])
        dp= [ [] for i in range(0,target+1)]
        for i in range(minDig,target+1):
            for candidate in digDict:
                if i == candidate:
                    dp[i].append([candidate])
                elif i > candidate:
                    gap = i - candidate
                    # if gap in digDict.keys():
                    possibilities = dp[gap]
                    for j in range(len(possibilities)):
                        newPos = list(possibilities[j])
                        newPos.append(candidate)
                        newPos.sort()
                        if newPos not in dp[i]:

                            dp[i].append(newPos)
        return dp[target]

s = Solution()
print(s.combinationSum([2,3,6,7],7))

