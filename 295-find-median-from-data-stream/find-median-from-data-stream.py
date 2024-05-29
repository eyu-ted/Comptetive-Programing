class MedianFinder:

    def __init__(self):
        self.minn = []
        self.maxx = []

    def addNum(self, num: int) -> None:

        if not self.maxx or -self.maxx[0]>=num:
            heappush(self.maxx,-1*num)
        else:
            heappush(self.minn,num)


        if len(self.minn) > len(self.maxx):
            heappush(self.maxx,-1*heappop(self.minn)) 
        elif len(self.maxx) > len(self.minn) +1:
            heappush(self.minn,-1*heappop(self.maxx)) 

        

    def findMedian(self) -> float:
        if len(self.minn) == len(self.maxx):
            return (self.minn[0] + (-1*self.maxx[0]))/2
        else:
            return -self.maxx[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()