class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d={}
        for task in tasks:
            d[task]=d.get(task,0)+1
        heap=[]
        for task in d:
            heapq.heappush(heap,-d[task])
        q=deque()
        t=0
        while heap or q:
            t+=1
            if not heap:
                t=q[0][0]
            else:
                freq=heapq.heappop(heap)
                freq+=1
                if freq:
                    q.append((t+n,freq))
            if q:
                if t == q[0][0]:
                    time, freq=q.popleft()
                    heapq.heappush(heap,freq)
        return t