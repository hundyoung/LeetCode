import numpy as np
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # if one of the strings is empty
        n = len(word1)
        m = len(word2)
        if n * m == 0:
            return n + m
        dp = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        # dp = np.array(dp)
        for i in range(len(dp)):
            dp[i][0] = i
        for j in range(len(dp[0])):
            dp[0][j] = j
        for i in range(1,len(dp)):
            for j in range(1,len(dp[i])):
                char_1 = word1[i-1]
                char_2 = word2[j-1]
                up = dp[i-1][j]+1
                left = dp[i][j-1]+1
                left_up = dp[i-1][j-1]
                if char_1!=char_2:
                    left_up +=1
                dp[i][j]=min(up,left,left_up)

        return dp[-1][-1]


s = Solution()
print(s.minDistance("horse", "ros"))
