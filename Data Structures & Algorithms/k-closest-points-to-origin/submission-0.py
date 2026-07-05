class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            dist=point[1]*point[1]+point[0]*point[0]
            if len(heap)<k:
                heapq.heappush(heap, (-dist,point))
            else:
                if -heap[0][0]>dist:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-dist,point))
               
        ans=[]
        for dist, point in heap:
            ans.append(point)
        return ans
