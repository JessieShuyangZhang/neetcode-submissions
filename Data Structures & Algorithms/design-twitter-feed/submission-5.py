class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.userTweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.userTweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId]
        users.add(userId)
        minhp = [] # only the 10 largest
        for user in users:
            usertweets = self.userTweets[user]
            for i in range(len(usertweets)-1, max(-1, len(usertweets)-11), -1):
                heapq.heappush(minhp, usertweets[i])
            while len(minhp) > 10:
                heapq.heappop(minhp)
                
        res = []
        while minhp:
            res.append(heapq.heappop(minhp)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

