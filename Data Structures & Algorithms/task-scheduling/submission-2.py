class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d={}
        for task in tasks:
            d[task]=d.get(task,0)+1
        heap=[]
        for task in d:
            heapq.heappush(heap,(-d[task],task))
        q=deque()
        t=0
        while heap or q:
            if heap:
                freq,task=heapq.heappop(heap)
                freq+=1
                if freq:
                    q.append((t+n,task,freq))
            if q:
                if t == q[0][0]:
                    time, task, freq=q.popleft()
                    heapq.heappush(heap,(freq,task))
            t+=1
        return t