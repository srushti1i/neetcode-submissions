class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        l = 0
        res = 0
        for r, c in enumerate(s):
            if c in chars and chars[c] >= l:
                l = chars[c] + 1
            chars[c] = r
            res = max(res, r - l + 1)
        return res