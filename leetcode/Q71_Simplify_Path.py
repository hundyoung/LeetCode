class Solution:
    def simplifyPath(self, path: str) -> str:
        dir_list= path.split('/')
        i = 0
        result_list =[]
        while i <len(dir_list):
            dir = dir_list[i]
            if dir:
                if dir!='.':
                    if dir=='..':
                        if len(result_list)>0:
                            result_list.pop(-1)
                    else:
                        result_list.append(dir)
            i+=1
        result =''
        for dir in result_list:
            result= result+'/'+dir
        if not result:
            result='/'
        return result
s= Solution()
print(s.simplifyPath("/../"))