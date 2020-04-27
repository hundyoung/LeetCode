class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # def getK(arr:list):
        #     max_value =-1
        #     max_index=-1
        #     search_coast=0
        #     for i in range(len(arr)):
        #         if max_value<arr[i]:
        #             max_value=arr[i]
        #             max_index=i
        #             search_coast+=search_coast+1
        #     return search_coast
        if n==1:
            return m
        self.count=0
        def back_track(len,max_value,count_k):
            if len==n and count_k==k:
                self.count+=1
            elif count_k>k or len>n:
                return
            else:
                for i in range(1,m+1):
                    if i<=max_value:
                        back_track(len+1,max_value,count_k)
                    else:
                        back_track(len+1,i,count_k+1)
        for i in range(1,m+1):
            back_track(1,i,1)
        return self.count &1e9+7
s = Solution()
n = 50
m = 10
k = 25
print(s.numOfArrays(n,m,k))