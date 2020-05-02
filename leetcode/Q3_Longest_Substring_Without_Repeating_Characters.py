class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        own_set=set()
        left =0
        right=1
        result=0
        while right<=len(s):
            if s[right-1] not in own_set or left==right:
                result=max(result,right-left)
                own_set.add(s[right-1])
                right+=1
            else:
                own_set.remove(s[left])
                left+=1
        return result
s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
