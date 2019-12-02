class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for i in range(len(s))]
        maxV = 0
        for i in range(1,len(s)):
            char = s[i]
            if char == ')':
                if s[i-1]=='(':
                    if i-2>=0:

                        dp[i] = dp[i-2]+2
                    else:
                        dp[i] = 2
                else:
                    # if dp[i-dp[i-1]]=="(":
                    #     dp[i] = dp[i-1]+2
                    # else:
                    #     dp[i] = 0
                    if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                        if i-dp[i-1]-2>=0:
                            dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
                        else:
                            dp[i] = dp[i-1]+2

                # lastRight = i
                maxV = max(maxV,dp[i])
        return maxV



solution = Solution()
print(solution.longestValidParentheses("(()))())("))