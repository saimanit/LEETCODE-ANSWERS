class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        start = max_length = 0
        for c in range(len(s)):
            if s[c] in char_index and char_index[s[c]] >= start:
                start = char_index[s[c]] +1
            char_index[s[c]] = c
            max_length = max(max_length, c-start+1)
        return max_length