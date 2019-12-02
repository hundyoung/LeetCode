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
            dividend = dividend-divisor
            result+=1
        if negativeFlag:
            result = 0 - result
        return result

solution = Solution()
print(solution.divide(-2147483648,-1))