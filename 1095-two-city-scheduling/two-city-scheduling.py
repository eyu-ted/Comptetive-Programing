class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        

        def my(lis):
            return lis[0] - lis[1]

        
        costs.sort(key = my)
        result = 0
        for i in range(len(costs)):
            if i<len(costs)//2:
                result += costs[i][0]
            else:
                result += costs[i][1]


        return result
