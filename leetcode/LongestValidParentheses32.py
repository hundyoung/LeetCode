class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longestLength = 0
        for i in range(len(s)):
            char = s[i]
            if char == '(':
                tempStack = []
                pairCount = 0
                tempStack.append(char)
                for j in range(i+1,len(s)):
                    currentChar = s[j]
                    if currentChar == '(':
                        tempStack.append(char)
                    else:
                        if len(tempStack)==0:
                            break
                        else:
                            pairCount+=2
                            tempStack.pop(-1)
                            if len(tempStack)==0:
                                longestLength = max(pairCount,longestLength)
        return longestLength

solution = Solution()
print(solution.longestValidParentheses(")(((((()())()()))()(()))("))