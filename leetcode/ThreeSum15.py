def findDigit(array,target):
    flag = False

    left = 0
    right = len(array)-1
    while left<=right:
        center = int((left+right)//2)
        if target < array[center]:
            right = center-1
        elif target>array[center]:
            left = center+1
        else:
            flag = True
            break
    return flag

nums=[-1, 0, 1, 2, -1, -4]
left = 0
right = len(nums)-1
nums.sort()
numsMap={}
result = []
for i in nums:
    numsMap[i] = i
while right-left>1:
    sum = 0-(nums[left]+nums[right])
    center = int((left+right)/2)
    # if sum>=nums[left] and sum<=nums[right] and sum in numsMap.keys():
    threeNums = [nums[left],sum,nums[right]]
    if findDigit(nums[left+1:right],sum) and threeNums not in result:
        result.append(threeNums)
    if sum>nums[center]:
        left = left+1
    else:
        right = right-1
# print(nums)
print(result)