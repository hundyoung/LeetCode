from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        dp=[[0]*(shelf_width+1) for _ in range(len(books))]
        dp[0][books[0][0]]=books[0][1]
        for i in range(len(books)):
            for j in range(1,shelf_width+1):
                if j-books[i][0]>=0:
                    pre=max(dp[i-1][j-books[i][0]])
                else:
                    pre=float('inf')
                dp[i][j]=min(pre,dp[i-1][j]+books[i][1])
