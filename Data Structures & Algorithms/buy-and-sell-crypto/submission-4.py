class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        best = 0
        l = 0
        r = 1
        cheap = prices[0]
        for pr in prices:
            
            if  pr < cheap:
                cheap = pr
            if best < pr - cheap:
                best = pr - cheap
        return best
