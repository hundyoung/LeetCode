from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        if len(books)==0:
            return 0
        dp=[float('inf')]*len(books)
        dp[0]=books[0][1]
        for i in range(1,len(books)):
            book_x,book_y = books[i]
            dp[i]=dp[i-1]+book_y
            temp_x=book_x
            temp_y=book_y
            for j in range(i-1,-1,-1):
                if temp_x+books[j][0]<=shelf_width:
                    temp_y=max(temp_y,books[j][1])
                    temp_x=temp_x+books[j][0]
                    if j-1>=0:
                        dp[i]=min(dp[i],dp[j-1]+temp_y)
                    else:
                        dp[i] = min(dp[i],temp_y)
                else:
                    break
        return dp[-1]
s = Solution()
print(s.minHeightShelves(books =[[1,3],[2,4],[3,2]], shelf_width = 6))
