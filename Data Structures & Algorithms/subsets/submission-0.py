class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(index, cur):
            if index==len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[index])
            backtrack(index+1, cur)

            cur.pop()
            backtrack(index+1,cur)
        backtrack(0,[])
        return res