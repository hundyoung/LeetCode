class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # nums = set(nums)
        # return len(nums)
        index = 1
        while index<len(nums):
            if nums[index]==nums[index-1]:
                del nums[index]
            else:
                index+=1
        return len(nums)



if __name__=="__main__":
    solution = Solution()
    nums = [1,1,2]
    length = solution.removeDuplicates(nums)
    for i in range(length):
        print(nums[i])