class Solution:
    def longestDupSubstring(self, S: str) -> str:
        left = 1
        right = len(S)
        dup_str = ''
        dup_length = -1
        sub_str_set=set()
        # pre_mid = -1
        while left<=right:
            mid = (left+right)>>1
            is_found = False
            for i in range(mid,len(S)+1):
                sub_string = S[i-mid:i]
                if sub_string not in sub_str_set:
                    sub_str_set.add(sub_string)
                else:
                    if mid>dup_length:
                        dup_length=mid
                        dup_str = sub_string
                    is_found=True
                    break
            if is_found:
                left = mid + 1
            else:
                right = mid - 1
        return dup_str
s = Solution()
print(s.longestDupSubstring("baaaaaababbbbbaaababaaabbabbabbbaabaaaaabbbaaababaabbbabbbabaaabbaabbabbbbbbbaabbabbabababbabbabaababbaabababbabbaabbabaaabbaaaaaaabbaabaabbababbabbbbaaaaabaabaaaabbabaaaabbbbbabaaabbababbbbaabbaabbaaaabbbbaabbababbaaabbbbabbabaaaaabbabaaaabaabaabbbabababaaababaabaabbabbbbaabbabbabaaaababbbaabbbbaaabbabbbbabbbaaaabbbaabbaabaaabaaaaaabbbbbabbbbbbabaabbbaababaaabbaabbabbbbbbbbbaaabaababaaabbbabaaaabbbabaaaabbbbaaaaaabbaaaaabbaaaababaaaaaaababbaaabbbbaababbaabbaababaaabaabbababbbabaaaabbbbaabbabaabbbaaaaabbabbbbbbabaaaaaaaabbaaabbbbbaabbaaababbaaaababbaaabbbbbbabbbbaabbaabababbbbaaaaaaaabaababaabbbababaabbaaaaabbaaabaaababbabbbabbbaaabaaaabbaabbaaabababbbaaaaaababaaabaabaababaaabbbbbbbbbbbaaabaaaabbaabababbaabbbbabbaabbaabaaaabbabbbbbaaaaaabbaabbabaabbbbbaabaabaabbababbbaaaabaaabbabbaaaaababbaabbabaaabbbabbaaababaaabbaaabbabbaababaaabbbabbabbbbaaaabbbaababbbababababaaababaaaababaababbaababbaaabaaaaababaababbaaabbbabaababababbabaabaaabaababaabbbaabaaaabaaabbbaabbbbbaaaaaabaabbabaaaabababa"))
