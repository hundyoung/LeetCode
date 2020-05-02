# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self,nums):
        self.array=nums

    def get(self, index: int) -> int:
       return self.array[index]
    def length(self) -> int:
       return len(self.array)

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        arr_len=mountain_arr.length()
        left=0
        right =arr_len-1
        n_max_index=0
        n_max=0
        while left<=right:
            mid = (left+right)>>1
            mid_val = mountain_arr.get(mid)
            if (mid-1>=0 and mountain_arr.get(mid-1)<mid_val) or (mid+1<arr_len and mountain_arr.get(mid+1)>mid_val):
                if mid_val==target:
                    return mid
                else:
                    if mid_val<target:
                        left=mid+1
                    else:
                        right=mid-1
            else:
                right=mid-1
            n_max_index=max(n_max_index,mid)
            n_max=max(n_max,mid_val)
        if target>n_max:
            return -1
        left=n_max_index
        right=arr_len-1
        while left<=right:
            mid = (left+right)>>1
            mid_val = mountain_arr.get(mid)
            if (mid-1>=0 and mountain_arr.get(mid-1)>mid_val) or (mid+1<arr_len and mountain_arr.get(mid+1)<mid_val):
                if mid_val==target:
                    return mid
                else:
                    if mid_val<target:
                        right=mid-1
                    else:
                        left=mid+1
            else:
                left=mid
        return -1
s=Solution()
m = MountainArray([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2])
print(s.findInMountainArray(22,m))


