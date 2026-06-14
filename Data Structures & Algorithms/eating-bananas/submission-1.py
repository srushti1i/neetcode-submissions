from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n=len(piles)
        count=0
        piles=sorted(piles)
        l,r=1, piles[-1]
        k=float('inf')
        while l<=r:
            count=0
            mid=(l+r)//2
            for i in range(n):
                count+=ceil(piles[i]/mid)
            if count>h:
                l=mid+1
            else:
                r=mid-1
            if mid<k and count<=h:
                k=mid
        return k
