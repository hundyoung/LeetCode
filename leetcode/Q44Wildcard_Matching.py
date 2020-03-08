class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s)==0 and (len(p)==0 or p=="*"):
            return True
        if len(p)==0:
            return False
        s = list(s)
        s.insert(0,"#")
        s.append("#")
        dp = [[False for j in range(len(s))]for i in range(len(p))]
        # print(dp)
        x = p[0]
        char = s[1]

        if x == char or (char != "#" and x == "?"):
            dp[0][1] = True
        else:
            if x == "*":
                dp[0][0] = True
                for k in range(0, len(dp[0])):
                    dp[0][k] = True
            else:
                return False
        for i in range(1,len(p)):
            x = p[i]
            for j in range(1,len(dp[i])):
                char = s[j]
                if dp[i-1][j-1]:
                    if x == char or (char != "#" and x == "?"):
                        dp[i][j] = True
                    elif x == "*":
                        for k in range(j-1, len(dp[i])):
                            dp[i][k] = True
                        break


        return dp[-1][-1] or dp[-1][-2]


solution = Solution()
# s="acdcb"
# p= "a*c?b"
s,p="aaab","b*"
print(solution.isMatch(s,p))