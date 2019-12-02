nums = [-1,0,1,1,55]
target = 3
nums.sort()
result = nums[0]+nums[1]+nums[2]
if target>nums[-1]+nums[-2]+nums[-3]:
    # return nums[-1]+nums[-2]+nums[-3]
    print(nums[-1]+nums[-2]+nums[-3])
for i in range(len(nums)):
    left = i+1
    right = len(nums)-1
    if i+2<len(nums) and target< nums[i]+nums[i+1]+nums[i+2] :
        if (result - target) ** 2 > (nums[i]+nums[i+1]+nums[i+2] - target) ** 2:
            result = nums[i]+nums[i+1]+nums[i+2]
        break
    while left<right:
        # if target>nums[right]:
        #     break
        sum = nums[i]+nums[left]+nums[right]
        if sum==target:
            result =target
            # return result
            break
        else:
            if target> nums[right]+nums[right-1]+nums[right-2]:
                if (result - target) ** 2 > (nums[right]+nums[right-1]+nums[right-2] - target) ** 2:
                    result = nums[right]+nums[right-1]+nums[right-2]
                break
            if (result-target)**2>(sum-target)**2:
                result=sum
            if target>sum:
                left+=1
            else:
                right-=1
print(result)
