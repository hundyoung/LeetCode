class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand_dict ={}
        for color in hand:
            if color not in hand_dict:
                hand_dict[color]=0
            hand_dict[color]+=1
        count=0
        def update(board,count):
            i=0
            color_map = {}
            array = []

            while i <len(board):
                color = board[i]
                j=i+1
                while j<len(board) and board[j]==color:
                    j+=1
                if j-i>=3:
                    color_map = {}
                    array = []

                    board=board[:i]+board[j:]
                    i=0
                    continue
                if color not in color_map:
                    color_map[color]= 0
                color_map[color] = color_map[color]+1
                array.append(board[i:j])
                i=j
            # print(color_map)
            if len(color_map)==0:
                return count
            color_list = sorted(color_map.items(),key=lambda x:x[1])
            for i in range(len(color_list)):
                color,_ = color_list[i]
                if hand_dict.setdefault(color,0)>0:
                    longest = 0
                    longest_j =0
                    for j in range(len(array)):
                        if color in array[j]:
                            current_length = len(array[j])
                            if current_length>longest:
                                longest=current_length
                                longest_j=j
                    dif = hand_dict[color] - (3-longest)
                    if dif>=0:
                        count=count+(3-longest)
                        hand_dict[color]=dif
                        array.pop(longest_j)
                        if len(array)>0:
                            count = update(''.join(array),count)
                            return count
                        else:
                            return count
            return -1
        count = update(board,count)
        return count

s = Solution()
print(s.findMinStep("WWGWGW","GWBWR"))