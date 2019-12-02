class Solution:
    def __init__(self):
        self.results = []
    def divide2ways(self,n,tempArray:list,result:str):
        if n==0:
            while len(tempArray)>0:
                tempArray.pop(-1)
                result+=")"
            self.results.append(result)
        else:
            if len(tempArray)!=0:
                tempResult = result
                tempResult+=")"
                newTempArray = list(tempArray)
                newTempArray.pop(-1)
                self.divide2ways(n,newTempArray,tempResult)
            tempArray.append("(")
            result+="("
            self.divide2ways(n-1, tempArray, result)

    def generateParenthesis(self, n: int):
        # tempArray = []
        self.divide2ways(n,[],"")
        return self.results

if __name__ == "__main__":
    solution = Solution()
    print(solution.generateParenthesis(1))