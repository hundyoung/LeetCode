class Solution:
    def reverseWords(self, s: str) -> str:
        s_groups = s.split()
        result_list = []
        for i in range(len(s_groups)):
            result_list.append(s_groups[i][::-1])
        return  ' '.join(result_list)
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))