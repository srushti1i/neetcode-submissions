class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        had=set()
        res=0
        l,r=0,0
        for r in range(len(s)):
            while s[r] in had:
                had.remove(s[l])
                l+=1
            had.add(s[r])
            res=max(res,r-l+1)
        return res