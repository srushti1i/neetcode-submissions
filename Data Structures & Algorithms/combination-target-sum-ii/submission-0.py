class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def backtrack(cur, index,left):
            if left==0:
                res.append(cur.copy())
                return
            if left<0:
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i]==candidates[i-1]:
                    continue
                cur.append(candidates[i])
                backtrack( cur,i+1, left-candidates[i])
                cur.pop()
        backtrack([],0, target)
        return res                
            