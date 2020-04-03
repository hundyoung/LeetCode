from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if len(folder)==0:
            return []
        folder = sorted(folder)
        prefix = folder[0].split('/')
        result = [folder[0]]
        for i in range(1,len(folder)):
            path = folder[i]
            dirs = path.split('/')
            # while dirs[0]=='':
            #     dirs.pop(0)
            is_prefix = True
            for j in range(min(len(prefix),len(dirs))):
                if prefix[j]!=dirs[j]:
                    is_prefix=False

            if not is_prefix:
                prefix =dirs
                result.append(path)
        return result
s= Solution()
folder = ["/aa/ab","/ah"]
print(s.removeSubfolders(folder))


