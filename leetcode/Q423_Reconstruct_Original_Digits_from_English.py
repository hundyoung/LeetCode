class Solution:
    def originalDigits(self, s: str) -> str:
        digit_dict = {}
        char_dict = {}
        # for i in range(10):
        #     digit_dict[i] = 0
        for i in range(len(s)):
            char = s[i]
            char_dict[char] = char_dict.get(char,0) + 1
        digit_dict[0] = char_dict.get('z',0)
        digit_dict[2] = char_dict.get('w',0)
        digit_dict[4] = char_dict.get('u',0)
        digit_dict[6] = char_dict.get('x',0)
        digit_dict[8] = char_dict.get('g',0)
        digit_dict[3] = char_dict.get('h',0)-digit_dict[8]
        digit_dict[1] = char_dict.get('o',0) - digit_dict[0] - digit_dict[2] - digit_dict[4]
        digit_dict[5] = char_dict.get('f',0) - digit_dict[4]
        digit_dict[7] = char_dict.get('s',0) - digit_dict[6]
        digit_dict[9] = char_dict.get('i',0) - digit_dict[8]-digit_dict[6]-digit_dict[5]
        result = ''
        for i in range(10):
            for j in range(digit_dict[i]):
                result+=str(i)
        return result

s= Solution()
print(s.originalDigits("fviefuro"))


