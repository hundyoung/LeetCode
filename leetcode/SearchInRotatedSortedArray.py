class Solution:
    def search(self, nums: list, target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            center = (int) ((right+left)/2)
            centerValue = nums[center]
            # if target<nums[center] and target>=nums[left]:
            #     right = center-1
            # elif target<nums[center] and target<nums[left]:
            #     left = center+1
            # elif target>nums[center] and target>nums[right]:
            #     left = center + 1
            # elif target>nums[center] and target<=nums[right]:
            #     left = center+1
            # elif target==nums[center]:
            #     return center

            # convert at right
            if target==centerValue:
                return center
            if centerValue>nums[left] and centerValue>nums[right]:

                if target < nums[center] and target >= nums[left]:
                    right = center - 1
                elif target < nums[center] and target < nums[left]:
                    left = center + 1
                elif target > nums[center] and target > nums[right]:
                    left = center + 1
                elif target > nums[center] and target <= nums[right]:
                    left = center + 1
            elif centerValue<nums[left] and centerValue<nums[right]:
                if target < nums[center] and target >= nums[left]:
                    right = center - 1
                elif target < nums[center] and target < nums[left]:
                    right = center - 1
                elif target > nums[center] and target > nums[right]:
                    right = center - 1
                elif target > nums[center] and target <= nums[right]:
                    left = center + 1
            else:
                if target < nums[center] and target >= nums[left]:
                    right = center - 1
                else:
                    left = center + 1

        return -1


solution = Solution()
print(solution.search([5,1,2,3,4],1))

