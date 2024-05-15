class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dic  = {}

        def dp(i):
            if i >= len(days) :
                return 0
            
            if i in dic:
                return dic[i]
            dic[i] = float("inf")

            for d,c in zip([1,7,30],costs):
                j =i 
                while j < len(days) and days[j] < days[i]+d:
                    j+=1
                
                dic[i] = min(dic[i], dp(j)+c)
            return dic[i]
            
        return dp(0)
    
        