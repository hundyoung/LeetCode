class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i=len(num1)-1
        j=len(num2)-1
        result = ''
        carry=0
        while i>=0 or j>=0:
            n_1 = num1[i] if i>=0 else 0
            n_2 = num2[j] if j>=0 else 0
            n_sum = int(n_1) + int(n_2) + carry
            carry = n_sum//10
            result = str(n_sum%10)+result
            i-=1
            j-=1
        if carry>0:
            result = str(carry)+result
        return result
s = Solution()
print(s.addStrings('1',"9"))
