from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people,key=lambda x:(x[1],-x[0]))
        result_list = []
        zero_list=[]
        while len(people)>0:
            height,higher_people = people.pop(0)
            higher_count = 0
            i=0
            # if higher_people>0:
            #     if len(zero_list) > 0:
            #         zero_list = sorted(zero_list, key=lambda x: x[0])
            #         result_list = result_list + zero_list
            #         zero_list=[]
            while i<len(result_list):
                if higher_count==higher_people:
                    break
                if result_list[i][0]>=height:
                    higher_count+=1
                i+=1
            result_list.insert(i, [height, higher_people])
        #     else:
        #         zero_list.append([height,higher_people])
        # if len(zero_list)>0:
        #     zero_list =sorted(zero_list, key=lambda x: x[0])
        #     result_list=result_list+zero_list
        return result_list
s = Solution()
print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))


