class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)):
            j=1
            count+=1
            while i-j>=0 and i+j<len(s) and s[i-j]==s[i+j]:
                count+=1
                j+=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
                j=1
                while i - j -1 >= 0 and i + j < len(s) and s[i - j -1] == s[i + j]:
                    count += 1
                    j+=1
        return count
s = Solution()
print(s.countSubstrings('aaabbb'))