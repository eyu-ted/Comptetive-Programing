class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxx=float("-inf")
        for trip in trips:
            maxx=max(maxx,trip[2])
        prefsum=[0]*(maxx+2)

        for trip in trips:
            if trip[0]>capacity:
                return False
            prefsum[trip[1]]+=trip[0]
            prefsum[trip[2]]-=trip[0]
        
        for i in range(1,len(prefsum)):
            prefsum[i]+=prefsum[i-1]
            if prefsum[i] > capacity:
                return False
        return True
        
