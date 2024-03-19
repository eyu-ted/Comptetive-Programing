class TimeMap:

    def __init__(self):
        self.dic = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key][0].append(value)
            self.dic[key][1].append(timestamp)
        else:
            self.dic[key]=[[value],[timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""
        arr = self.dic[key]
        index = bisect_right(arr[1],timestamp)  
        return arr[0][index-1] if index-1>=0 else ""










# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)