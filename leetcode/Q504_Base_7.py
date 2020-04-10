class Solution:
    def convertToBase7(self, num: int) -> str:
        base_7 = []
        negative = False
        if num<0:
            negative= True
            num= -num
        while num>=7:
            mod = num%7
            base_7.append(str(mod))
            num = num//7
        base_7.append(str(num))
        result = ''.join(base_7[::-1])
        if  negative:
            result = "-"+result
        return result
s =Solution()
print(s.convertToBase7(-7))