# leet code
# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i = 0
        while(i < len(s)):
            j = i
            while(j < len(s)):

                sub_str = s[i : j + 1]

                if(len(sub_str) == len(set(sub_str))):
                    if(len(sub_str) > max_len):
                        max_len = len(sub_str)
                else:
                    break
                j += 1
            i += 1


        return max_len
