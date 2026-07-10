class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        base={}
        if len(s)!=len(t):
            return False
        for char in s:
            base[char]=base.get(char,0)+1
        need={}
        has=len(base)
        for char in t:
            if char not in base:
                return False
            need[char]=need.get(char,0)+1
            if need[char]==base[char]:
                has-=1
        if has==0:
            return True
        else:
            return False