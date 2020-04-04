class Solution:
    def isHappy(self, n: int) -> bool:
        done = set()
        while True:
            s = str(n)
            total = 0
            for i in range(len(s)):
                char = s[i]
                total+=int(char)**2
            if total==1:
                return True
            else:
                if total not in done:
                    done.add(total)
                    n = total

                else:
                    return False
s = Solution()
print(s.isHappy(2))