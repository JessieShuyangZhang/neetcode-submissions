class Twitter:

    def __init__(self):
        self.follows = defaultdict(set) # userId -> set(userIds)
        self.usertweets = defaultdict(list) # userId -> list([time,tweetId])
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.usertweets[userId].append([self.time,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        followingset = self.follows[userId]
        followingset.add(userId)
        minheap = []
        for user in followingset:
            tws = self.usertweets[user]
            for tw in tws:
                heapq.heappush(minheap,(-tw[0],tw[1]))
        res, k = [], 10

        while minheap and k>0:
            res.append(heapq.heappop(minheap)[1])
            k -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
