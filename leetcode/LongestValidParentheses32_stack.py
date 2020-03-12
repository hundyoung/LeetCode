class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longestLen = 0
        tempStack = [-1]
        for i in range(len(s)):
            char = s[i]
            if char=="(":
                tempStack.append(i)
            else:
                tempStack.pop(-1)
                if len(tempStack)==0:
                    tempStack=[i]
                else:
                    longestLen = max(longestLen, i-tempStack[-1])

        return longestLen

solution = Solution()
print(solution.longestValidParentheses(")()())"))