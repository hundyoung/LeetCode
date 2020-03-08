class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        sum_list = []
        for i in range(len(num2)-1,-1,-1):
            inner_sum_list=[]
            n2 = int(num2[i])*(10**(len(num2)-i-1))
            for j in range(len(num1)-1,-1,-1):
                n1 = int(num1[j])*(10**(len(num1)-1-j))
                inner_two_sum = n2*n1
                inner_sum_list.append(inner_two_sum)
            sum_list.append(sum(inner_sum_list))
        return str(sum(sum_list))


s = Solution()
num1="9"
num2="99"
print(s.multiply(num1,num2))