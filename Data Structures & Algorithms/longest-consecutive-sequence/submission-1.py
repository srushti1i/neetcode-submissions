class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        if not nums:
            return 0
        res=1
        m=0
        for i in range(len(nums)-1):
            if(nums[i+1]-nums[i]==1):
                res+=1
            elif(nums[i+1]-nums[i]==0):
                continue
            else:
                if res>m:
                    m=res;
                res=1
        return max(res,m)