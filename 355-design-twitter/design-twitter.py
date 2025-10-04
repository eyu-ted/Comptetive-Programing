class Twitter:

    def __init__(self):
        self.follow_book = defaultdict(set)
        self.post_book = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time +=1
        self.post_book[userId].append([self.time,tweetId])
        # print(self.time , self.post_book)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        followee = list(self.follow_book[userId])
        soln = []
        soln.extend(self.post_book[userId])
        for followeeId in followee:
            soln.extend(self.post_book[followeeId])
        soln.sort()
        # print(soln)

        result = []
        for time, tweetid in soln[::-1][:10]:
            result.append(tweetid)
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_book[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in  self.follow_book:
            self.follow_book[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)