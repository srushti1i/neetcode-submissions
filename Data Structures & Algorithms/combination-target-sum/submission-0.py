class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(cur, index,left):
            if left==0:
                res.append(cur.copy())
                return
            if left<0 or index>=len(nums):
                return
            cur.append(nums[index])
            backtrack(cur, index, left-nums[index])
            cur.pop()
            backtrack(cur, index+1, left)
        backtrack([],0, target)
        return res
            