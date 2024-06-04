class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        c= 0
        ans = 0
        t= 0
        for num in happiness:
            if num-c>0:
                ans += (num-c)
            c+=1
            t+=1
            if t==k:
                return ans
        

        