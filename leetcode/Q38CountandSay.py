class Solution:
    def countAndSay(self, n: int) -> str:
        count = 1
        tempArray = ["1"]
        while count<n:
            newArray = []
            while len(tempArray)>0:

                ele = tempArray.pop(0)
                innerCount = 1
                while len(tempArray)>0 and tempArray[0]==ele:
                    tempArray.pop(0)
                    innerCount+=1
                newArray.append(str(innerCount))
                newArray.append(ele)
            tempArray=newArray
            count+=1
        return "".join(tempArray)

solution = Solution()
print(solution.countAndSay(4))