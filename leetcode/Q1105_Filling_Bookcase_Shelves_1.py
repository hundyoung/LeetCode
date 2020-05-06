from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        pre_not_new_row_x=float('inf')
        pre_not_new_row_y=float('inf')
        pre_new_row_x,pre_new_row_y=books[0]
        for i in range(1,len(books)):
            book_x,book_y=books[i]
            cur_not_new_row_x=float('inf')
            cur_not_new_row_y=float('inf')
            if book_x+pre_not_new_row_x<=shelf_width:
                cur_not_new_row_x=pre_not_new_row_x+book_x
                cur_not_new_row_y=pre_not_new_row_y+book_y-books[i-1][1] if book_y-books[i-1][1]>=0 else pre_not_new_row_y
            if book_x+pre_new_row_x<=shelf_width and max(pre_new_row_y,pre_new_row_y+book_y-books[i-1][1])<=cur_not_new_row_y:
                cur_not_new_row_x=pre_new_row_x+book_x
                cur_not_new_row_y=max(pre_new_row_y,pre_new_row_y+book_y-books[i-1][1])
            cur_new_row_x=book_x
            cur_new_row_y=min(pre_not_new_row_y,pre_new_row_y)+book_y
            pre_not_new_row_x=cur_not_new_row_x
            pre_not_new_row_y=cur_not_new_row_y
            pre_new_row_x, pre_new_row_y=cur_new_row_x,cur_new_row_y
        return min(pre_not_new_row_y,pre_new_row_y)
s = Solution()
print(s.minHeightShelves(books =[[9,9],[5,4],[3,1],[1,5],[7,3]], shelf_width = 10))
