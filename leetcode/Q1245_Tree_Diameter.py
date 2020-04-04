from typing import List

import copy
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj_dict = {}
        for i in range(len(edges)):
            left, right = edges[i]
            adj_set = adj_dict.get(left,set())
            adj_set.add(right)
            adj_dict[left] = adj_set
            adj_set = adj_dict.get(right, set())
            adj_set.add(left)
            adj_dict[right] = adj_set

        self.deepest_level = 0
        self.deep_node = 0
        def dfs(level,current_node,done:set):
            adj_set = adj_dict[current_node]
            if self.deepest_level<level:
                self.deepest_level = level
                self.deep_node = current_node
            for node in adj_set:
                if node not in done:
                    next_done = copy.deepcopy(done)
                    next_done.add(node)
                    dfs(level+1,node,next_done)
        # for node in adj_dict:
        #     done_set = set()
        #     done_set.add(node)
        #     adj_set = adj_dict[node]
        #     if len(adj_set)==1:
        #         dfs(0,node,done_set)
        done_set = set()
        done_set.add(0)
        dfs(0, 0, done_set)
        done_set = set()
        done_set.add(self.deep_node)
        dfs(0, self.deep_node, done_set)
        return self.deepest_level
s = Solution()
edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
print(s.treeDiameter(edges))