class Solution:
    def lastSubstring(self, s: str) -> str:
        if len(s)==0:
            return ''
        left, right = max(len(s)-2,0),len(s)-1
        def compare(a,b):
            for i in range(min(len(a),len(b))):
                if ord(a[i])>ord(b[i]):
                    return 1
                elif ord(a[i])<ord(b[i]):
                    return -1
                else:
                    continue
            if len(a)>len(b):
                return 1
            elif len(a)<len(b):
                return -1
            else:
                return 0
        while left>=0:
            if ord(s[left])>ord(s[right]):
                right=left
            elif ord(s[left])==ord(s[right]):
                left_left = left-1
                while left_left>=0 and ord(s[left_left])>=ord(s[left])  :
                    left=left_left
                    left_left-=1
                if ord(s[left])==ord(s[right]):
                    if compare(s[left:],s[right:])>=0:
                        right=left
                elif ord(s[left])>ord(s[right]):
                    right = left
            left-=1
        return s[right:]
s = Solution()
print(s.lastSubstring("vnhfleqyxj"))




