class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        count=0
        l,r=1, max(piles)
        k=float('inf')
        while l<=r:
            count=0
            mid=(l+r)//2
            for i in range(n):
                count+=math.ceil(piles[i]/mid)
            if count<=h:
                k=mid
                r=mid-1
            else:
                l=mid+1
        return k
