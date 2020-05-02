class Solution:
    def reformat(self, s: str) -> str:
        digits =[]
        alphas=[]
        for i in range(len(s)):
            char = s[i]
            if char.isdigit():
                digits.append(char)
            else:
                alphas.append(char)
        if (len(alphas)-len(digits))**2>1:
            return ''
        if len(digits)<len(alphas):
            first = alphas
            second = digits
        else:
            first = digits
            second = alphas
        result=''
        for i in range(max(len(alphas),len(digits))):
            result+=first[i]
            if i < len(second):
                result+=second[i]
        return result
s = Solution()
print(s.reformat("0"))


