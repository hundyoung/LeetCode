class Solution:
    def isValid(self, s: str) -> bool:
        array = []
        leftSym = ['(', '{' , '[' ]
        rightSym = [')', '}', ']']
        flag = True
        for i in range(len(s)):
            char = s[i]
            if char in leftSym:
                array.append(char)
            else:
                if len(array)<1:
                    flag=False
                    break
                lastChar = array.pop(-1)
                if lastChar == "(" and char == ")":
                    continue
                elif lastChar == "{" and char == "}":
                    continue
                elif lastChar == "[" and char == "]":
                    continue
                else:
                    flag = False
                    break
        if len(array)>0:
            flag=False
        return flag


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid("{[]}"))