class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        s = s.replace(' ', '')
        nums = []
        operations = []
        i = 0
        while i < len(s):
            if s[i] in ['+', '-', '*', '/']:
                operations.append(s[i])
                i += 1
            else:
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    j += 1
                nums.append(int(s[i:j]))
                i = j

        i = 0
        while i < len(operations):
            if operations[i] in ['*', '/']:
                operation = operations.pop(i)
                left = nums.pop(i)
                right = nums.pop(i)
                if operation=='*':
                    new_n = left*right
                else:
                    new_n = left//right
                nums.insert(i,new_n)
            else:
                i+=1
        i=0
        result = nums.pop(0)
        while i < len(operations):
            operation = operations.pop(0)
            right = nums.pop(0)
            if operation == '+':
                result = result + right
            else:
                result = result - right
        return result


s = Solution()
print(s.calculate(" 3+5 / 2 "))
