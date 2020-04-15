import copy
class Solution:
    def findIntegers(self, num: int) -> int:
        if num==0:
            return 1
        elif num==1:
            return 2

        target = bin(num).split('b')[1]
        pre_zero_one = [0,1]
        count=2
        dp = [[0,0]]*(len(target)+1)
        dp[1]=[0,1]
        count=2
        for i in range(2,len(target)+1):
            dp[i]=[sum(dp[i-1]),dp[i-1][0]]
            count+=sum(dp[i])
        # delete_count=0
        for i in range(1,len(target)):
            n = int(target[i])
            if n==1 and target[i-1]=='1':
                break
            elif n==0 and target[i-1]=='0':
                gap = len(target)-i
                count=count-sum(dp[gap])
        return count
s =Solution()
print(s.findIntegers(2))