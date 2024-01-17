class Robot:


    def __init__(self, width: int, height: int):
        self.dirs = {0: "East", 1: "North", 2: "West", 3: "South"}
        self.pos = 0
        self.dir = 0
        self.w = width - 1
        self.h = height - 1
        self.m = height + width - 2

    def step(self, num: int) -> None:
        self.pos += num
        self.pos %= (self.m * 2)
        if self.pos > self.m + self.w:
            self.dir = 3
        elif self.pos > self.m:
            self.dir = 2
        elif self.pos > self.w:
            self.dir = 1
        elif not self.pos:
            self.dir = 3
        else:
            self.dir = 0

    def getPos(self) -> List[int]:
        if self.pos > self.m + self.w:
            return [0,self.h - (self.pos - self.m - self.w)]
        elif self.pos > self.m:
            return [self.w - (self.pos - self.m) ,self.h]
        elif self.pos > self.w:
            return [self.w, self.pos - self.w ]
        else:
            return [self.pos,0]

    def getDir(self) -> str:
        return self.dirs[self.dir]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()