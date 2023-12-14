class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive=timeToLive
        self.dic={}
        
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.dic[tokenId]=currentTime
                

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.dic:
            if currentTime-self.dic[tokenId]<self.timeToLive:
                self.dic[tokenId]=currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count=0
        for value in self.dic.values():
            if value+self.timeToLive >currentTime:
                count+=1
        return count


        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)