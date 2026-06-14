class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        has={}
        pres={}
        for char in s:
            has[char]=has.get(char,0)+1
        need=len(has)
        for char in t:
            if char in has:
                pres[char]=pres.get(char,0)+1
                if pres[char]==has[char]:
                    need-=1
            else:
                return False
        if need==0:
            return True
        else:
            return False