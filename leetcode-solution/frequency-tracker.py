class FrequencyTracker:

    def __init__(self):
        self.frequencylist=[0] *(10**5+1)
        self.dic={}
        

    def add(self, number: int) -> None:
        freq=self.dic.get(number,0)
        if freq>0 and self.frequencylist[freq]>0:
            self.frequencylist[freq]-=1
        self.dic[number]=freq+1
        self.frequencylist[self.dic[number]]+=1
        

    def deleteOne(self, number: int) -> None:
        freq=self.dic.get(number,0)
        if freq>0:
            self.frequencylist[freq]-=1
            if freq==1:
                del self.dic[number]
            else:
                self.dic[number]=freq-1
                self.frequencylist[self.dic[number]]+=1
        

    def hasFrequency(self, frequency: int) -> bool:
        return frequency <len(self.frequencylist) and self.frequencylist[frequency]!=0
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)