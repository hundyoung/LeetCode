class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        done_set=[True]*n
        index=0
        total_count=0
        while total_count<n-1:
            count=0
            while count<m-1 or not done_set[index]:
                if done_set[index]:
                    count+=1
                index=index+1 if index+1<n else 0
            total_count+=1
            done_set[index]=False
        return done_set.index(True)

s =Solution()
print(s.lastRemaining(10,17))