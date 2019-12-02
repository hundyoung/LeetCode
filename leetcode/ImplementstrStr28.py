class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        if len(haystack)==0 and len(needle)==0:
            return 0
        if len(haystack)<len(needle):
            return -1
        while i < len(haystack):
            flag= True
            if len(haystack)-i<len(needle):
                return -1
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    flag=False
                    break
            if flag:
                break
            i+=1
        if i== len(haystack):
            return -1
        return i


solution = Solution()
print(solution.strStr("mississippia","a"))

