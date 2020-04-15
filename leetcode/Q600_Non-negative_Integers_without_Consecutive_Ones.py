import copy
class Solution:
    def findIntegers(self, num: int) -> int:
        if num==0:
            return 1
        elif num==1:
            return 2
        target = bin(num).split('b')[1]
        pre_zero_one = [0,1]
        count = 2
        for i in range(1,len(target)-1):
            pre_zero_one=[pre_zero_one[0]+pre_zero_one[1],pre_zero_one[0]]
            count+=sum(pre_zero_one)
        result = ['1']
        for i in range(1,len(target)):
            next_result = []
            for s in result:
                temp = s
                temp+='0'
                next_result.append(temp)
                temp = s
                if temp[-1]!='1':
                    temp+='1'
                    next_result.append(temp)
            result=next_result
        for i in range(len(result)):
            if int(result[i])<=int(target):
                count+=1
        return count
s =Solution()
print(s.findIntegers(5))