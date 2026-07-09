class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(arr, cur):
            if not arr:
                res.append(cur.copy())
                return
            for i in range(len(arr)):
                cur.append(arr[i])
                rem=arr[:i]+arr[i+1:]
                backtrack(rem,cur)
                cur.pop()
        backtrack(nums, [])
        return res