from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        tree = {}
        for i in range(len(ppid)):
            children=tree.get(ppid[i],set())
            children.add(pid[i])
            tree[ppid[i]]=children
        for i in range(len(pid)):
            if pid[i] not in tree:
                tree[pid[i]] = set()
        toProcess = [kill]
        result = []
        while len(toProcess)>0:
            node = toProcess.pop(0)
            for item in tree[node]:
                toProcess.append(item)
            result.append(node)
        return result
s =Solution()
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
print(s.killProcess(pid,ppid,kill))