class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [ 0 for _ in range(len(s))]
        if len(s)>0:
            if s[0]!='0':
                dp[0]=1
            else:
                return 0
        if len(s)>1:
            if s[1]!='0' and int(s[0]+s[1])<=26:
                dp[1]=2
            else:
                if s[1]=='0' and int(s[0]+s[1])>26:
                    dp[1]=0
                else:
                    dp[1]=1
        for i in range(2,len(s)):
            if s[i]!='0'and  s[i-1] != '0' and int(s[i-1]+s[i])<=26:
                dp[i] =  dp[i-1] + dp[i-2]
            else:
                if int(s[i])==0 :
                    if s[i-1]=='0':
                        dp[i] = 0
                    elif int(s[i-1]+s[i])>26:
                        dp[i] = 0
                    else:
                        if s[i-2]=='0':
                            dp[i] = dp[i-2]
                        elif int(s[i-2]+s[i-1])>26:
                            dp[i] = dp[i-2]
                        else:
                            dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[-1]

s= Solution()
print(s.numDecodings("227"))