class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def backtrack(index, cur):
                
            res.append(cur.copy())
            for i in range(index, len(nums)):
                if i > index and nums[i]==nums[i-1]:
                    continue
                cur.append(nums[i])
                backtrack(i+1, cur)
                cur.pop()
        backtrack(0,[])
        return res