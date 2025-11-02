class UndergroundSystem:

    def __init__(self):
        self.dic = {}
        self.summ = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dic[id] = (stationName,t)       

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.dic[id][0], stationName) not in self.summ:
            self.summ[(self.dic[id][0], stationName)] = [t- self.dic[id][1],1]
        else:
            self.summ[(self.dic[id][0], stationName)][0] += t- self.dic[id][1]
            self.summ[(self.dic[id][0], stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.summ[(startStation, endStation)][0] /self.summ[(startStation, endStation)][1] 
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)