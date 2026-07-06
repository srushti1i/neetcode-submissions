class Twitter:

    def __init__(self):
        self.following=defaultdict(set)
        self.tweet=defaultdict(list)
        self.timestamp=0
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp-=1
        self.tweet[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        heap=[]
        users=list(self.following[userId])
        users.append(userId)

        for user in users:
            if user in self.tweet:
                index=len(self.tweet[user])-1
                timestamp, tweetId=self.tweet[user][index]
                heapq.heappush(heap,(timestamp, tweetId, user, index-1))

        while heap and len(res)<10:
            timestamp, tweetId, user, index=heapq.heappop(heap)
            res.append(tweetId)
            if index>=0:
                next_time, next_timestamp=self.tweet[user][index]
                heapq.heappush(heap,(next_time, next_timestamp, user, index-1))
        return res
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
