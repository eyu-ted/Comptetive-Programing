class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step=0
        mem=capacity
        for i in range(len(plants)):
            step+=1
            capacity-=plants[i]
            if i+1<len(plants) and plants[i+1]>capacity:
                step+=(i+1)*2
                capacity=mem
        return step
          

        