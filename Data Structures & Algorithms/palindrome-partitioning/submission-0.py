class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def palindrome(sub):
            return sub==sub[::-1]
        def backtrack(i,path):
            if i==len(s) :
                res.append(path.copy())
                return
            for j in range(i,len(s)):
                if palindrome(s[i:j+1]):
                    path.append(s[i:j+1])
                    backtrack(j+1, path)
                    path.pop()
        backtrack(0, []) 
        return res               