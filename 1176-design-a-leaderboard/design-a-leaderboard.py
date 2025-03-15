class Leaderboard:

    def __init__(self):
        self.dic = defaultdict(int)
        

    def addScore(self, playerId: int, score: int) -> None:
        self.dic[playerId] += score
        # print(self.dic)
        

    def top(self, K: int) -> int:
        heap = []

        for val in self.dic.values():
            heappush(heap , val)
            if len(heap) > K:
                heappop(heap)
            
        
        return sum(heap)
        

        

    def reset(self, playerId: int) -> None:
        self.dic[playerId] = 0
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)