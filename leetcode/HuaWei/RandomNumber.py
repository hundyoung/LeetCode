from sys import stdin

class Solution(object):
    def getResult(self):
        nums = set()
        while True:
            line = stdin.readline().strip()
            if line == '':
                break
            else:
                nums.add(int(line))
        nums_list = sorted(nums)
        for n in nums_list:
            print(n)
if __name__=='__main__':
    s = Solution()
    s.getResult()

