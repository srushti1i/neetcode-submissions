class Solution:
    def findMin(self, nums: List[int]) -> int:
        a, b = 0, len(nums)-1
        m = (a+b) // 2
        if nums[a] <= nums[b]:
            return nums[a]
            

        while True:
            if nums[a] > nums[m] and \
                nums[b] > nums[m]:
                b = m
            elif nums[a] < nums[m] and \
                nums[b] < nums[m]:
                a = m
            else:
                return nums[m+1]
            m = (a+b) // 2