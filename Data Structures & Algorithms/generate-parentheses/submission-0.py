class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(cur, l, r):
            if len(cur)==2*n:
                res.append(cur)
                return
            if l<n:
                backtrack(cur+"(", l+1, r)
            if r<l:
                backtrack(cur+")", l,r+1)

        backtrack("",0,0)
        return res