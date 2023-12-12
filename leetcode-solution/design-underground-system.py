class UndergroundSystem:

    def __init__(self):
        self.dic={}
        self.dicavg={}
        self.dicsum={}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dic[id]=[stationName,t]


        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        dist=t-self.dic[id][1]
        self.dicsum[(self.dic[id][0],stationName)]=dist+self.dicsum.get((self.dic[id][0],stationName),0)
        self.dicavg[(self.dic[id][0],stationName)]=1+self.dicavg.get((self.dic[id][0],stationName),0)
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.dicsum[(startStation,endStation)]/self.dicavg[(startStation,endStation)]

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)