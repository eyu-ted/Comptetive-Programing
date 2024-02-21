class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        def my(n):
            return n[0]-n[1]
            
        costs.sort( key=my)
        print(costs)
        c=0
        tot=0
        for arr in costs:
            if c<len(costs)//2:
        
                tot+=arr[0]
            else:
                tot+=arr[1]
            c+=1
        return tot