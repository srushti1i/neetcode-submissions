class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums=[-x for x in stones]
        heapq.heapify(nums)
        while len(nums)>=2:
            x=-(heapq.heappop(nums))
            y=-(heapq.heappop(nums))
            if x>y:
                heapq.heappush(nums,-(x-y))
            elif x<y:
                heapq.heappush(nums,-(y-x))
        if not nums:
            return 0
        else:
            return -nums[0]