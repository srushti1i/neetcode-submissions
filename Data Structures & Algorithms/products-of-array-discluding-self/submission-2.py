class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        a=[0]*n
        b=[0]*n
        
        a[0]=nums[0]
        b[n-1]=nums[n-1]
        res=[0]*n
        for i in range(1,len(nums)):
            a[i]=a[i-1]*nums[i]
        print(a)
        for i in range(len(nums)-2,-1,-1):
            b[i]=b[i+1]*nums[i]
        print(b)
        res[0]=b[1]
        res[n-1]=a[n-2]
        for i in range(1,n-1):
            res[i]=a[i-1]*b[i+1]
        return res



        