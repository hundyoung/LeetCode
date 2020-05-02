class Solution:
    def reverseWords(self, s: str) -> str:
        s_groups=s.split(' ')
        result = ''
        for i in range(len(s_groups)-1,-1,-1):
            word = s_groups[i]
            if word!='':
                result+=word+' '
        return result[:-1]
s = Solution()
print(s.reverseWords("a good   example"))
