class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_win=float('inf')
        cs={}
        count=Counter(t)
        l=0
        need=len(count)
        have=0
        res=''
        for r in range(len(s)):
            c=s[r]
            cs[c]=cs.get(c,0)+1
            if c in count and cs[c]==count[c]:
                have+=1
            while have==need:
                if (r-l+1)<min_win:
                    min_win=r-l+1
                    res=s[l:r+1]
                cs[s[l]]-=1
                if s[l] in count and cs[s[l]]<count[s[l]]:
                    have-=1
                l+=1
        return res
                    
