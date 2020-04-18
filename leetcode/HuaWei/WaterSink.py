
line = input()
n_str = line.split(',')
nums = list(map(lambda x:int(x),n_str))
max_water = 0
for i in range(len(nums)):
    height_left = nums[i]
    for j in range(i+1,len(nums)):
        height_right = nums[j]
        max_water=max(max_water,(j-i)*min(height_left,height_right))
print(max_water)
