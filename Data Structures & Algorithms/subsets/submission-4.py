class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(path, nums):
            ans.append(path.copy())        
            for i, num in enumerate(nums):

                path.append(num)
                backtrack(path, nums[i+1:])
                path.pop()
            
        backtrack([], nums)
        return ans