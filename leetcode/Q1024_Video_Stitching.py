from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips=sorted(clips,key=lambda x:(x[1],x[0]))
        # clips=sorted(clips,key=lambda x:(x[0],-x[1]))
        count=1
        index=-1
        start_max_end=0
        for i in range(len(clips)):
            if clips[i][0]==0 and clips[i][1]>start_max_end:
                index=i
                start_max_end=clips[i][1]
        if index==-1:
            return -1
        while index<len(clips)-1:
            current_interval=clips[index]
            end = current_interval[1]
            if end>=T:
                break
            next_index=-1
            for j in range(len(clips)-1,index,-1):
                next_interval = clips[j]
                if next_interval[0]<=end:
                    next_index=j
                    break
            if next_index!=-1:
                index=next_index
                count+=1
            else:
                break
        if clips[index][1]<T:
            return -1
        else:
            return count
s = Solution()
print(s.videoStitching([[0,0],[9,9],[2,10],[0,3],[0,5],[3,4],[6,10],[1,2],[4,7],[5,6]],5))


