from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        table_dict = {}
        food_set=set()
        for name,table,food in orders:
            table=int(table)
            table_food_dict = table_dict.get(table,{})
            table_food_dict[food] = table_food_dict.get(food,0)+1
            table_dict[table]=table_food_dict
            food_set.add(food)
        table_list = sorted(table_dict.keys())
        result=[]
        food_list=sorted(list(food_set))
        result.append(food_list)
        for table in table_list:
            table_food_dict=table_dict[table]
            inner_result=[str(table)]
            for food in food_list:
                inner_result.append(str(table_food_dict.get(food,0)))
            result.append(inner_result)
        header=result[0]
        header.insert(0,'Table')
        return result
s = Solution()
orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]

print(s.displayTable(orders))
