class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        negative = []
        possitive = []
        zero = []
        dic = {}
        result = {}
        for num in nums:
            if num<0:
                negative.append(num)
            elif num>0:
                possitive.append(num)
            else:
                zero.append(num)
            if num in dic.keys():
                dic[num] = dic[num] + 1
            else:
                dic[num] = 1
        if 0 in dic.keys() and dic[0] >2:
            result.append([0,0,0])
        negative = list(set(negative))
        possitive = list(set(possitive))
        # negative.sort()
        # possitive.sort()
        # print(possitive)
        for i in range(len(negative)):
            for j in range(len(possitive)-1,-1,-1):
                sum = 0-negative[i] - possitive[j]
                if sum in dic.keys():
                    array = []
                    if dic[sum] >1:
                        array = [negative[i],possitive[j],sum]
                    elif dic[sum] ==1:
                        if sum>0 and possitive[j] != sum:
                            array = [negative[i],possitive[j],sum]
                        elif sum<0 and negative[i] != sum:
                            array = [negative[i],possitive[j],sum]
                        elif sum ==0:
                            array = [negative[i],possitive[j],sum]
                        else:
                            continue
                    else:
                        continue
                    array.sort()
                    result[str(array[0])+]
                else:
                    continue
        # print(result)
        return result


    print(threeSum(None,[3,0,-2,-1,1,2]))

