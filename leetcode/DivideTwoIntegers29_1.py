class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negativeFlag = False
        if dividend>0 and divisor<0:
            divisor = 0 - divisor
            negativeFlag = True
        elif dividend<0 and divisor>0:
            dividend = 0 - dividend
            negativeFlag=True
        elif dividend<0 and divisor<0:
            divisor = 0 - divisor
            dividend = 0 - dividend

        result = 0
        while dividend>=divisor:
            tempDivisor = divisor
            divisorCount = 1
            while dividend>= tempDivisor:
                dividend = dividend-tempDivisor
                result+=divisorCount
                divisorCount +=divisorCount
                tempDivisor += tempDivisor
        if negativeFlag:
            result = 0 - result
        return min(max((-2)**31,result),2**31-1)

solution = Solution()
print(solution.divide(-2147483648,-1))