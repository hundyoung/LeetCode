class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        for char in s:
            count = char_dict.get(char,0)+1
            char_dict[char]=count
        for i in range(len(s)):
            char =s[i]
            if char_dict[char]==1:
                return i
        return -1
s = Solution()
print(s.firstUniqChar("aadadaad"))