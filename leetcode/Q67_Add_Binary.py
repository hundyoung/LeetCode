class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = 1
        add_one = 0
        result = []
        while i<=len(a) and i<=len(b):
            n_a,n_b = int(a[-i]),int(b[-i])
            s =  n_a+n_b+add_one
            if s>1:
                add_one=1
                s-=2
            else:
                add_one=0
            result.insert(0,str(s))
            i+=1
        while i <= len(a):
            n_a = int(a[-i])
            s =  n_a+add_one
            if s>1:
                add_one=1
                s-=2
            else:
                add_one=0
            result.insert(0,str(s))
            i+=1
        while i <= len(b):
            n_b = int(b[-i])
            s =  n_b+add_one
            if s>1:
                add_one=1
                s-=2
            else:
                add_one=0
            result.insert(0,str(s))
            i+=1
        if add_one>0:
            result.insert(0,str(1))

        return ''.join(result)

s = Solution()
a = "1111"
b = "1111"
print(s.addBinary(a,b))
