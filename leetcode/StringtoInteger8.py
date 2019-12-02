class Solution:
    def myAtoi(self, str: str) -> int:
        str1 = str.strip()
        result = ""
        for i in range(len(str1)):
            char = str1[i]
            if(i==0and (char=="+" or char=="-")):
                result= result+char
            elif char.isdigit():
                result = result + char
            else:
                break
        # print(str1)
        try:
            result = int(result)
            result = min(2**31-1,result)
            result = max((-2)**31,result)
            return result
        except:
            return 0


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi("-5-"))