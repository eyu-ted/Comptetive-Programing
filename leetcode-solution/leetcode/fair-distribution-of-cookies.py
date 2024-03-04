class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        self.minn = float("inf")
        bucket = [0]*k
        cookies.sort(reverse = True)


        def back(i):
            if i >= len(cookies):
                self.minn = min(self.minn,max(bucket))
                return 
            
            
            for j in range(k):
                if bucket[j] + cookies[i] >= self.minn or (j > 0 and bucket[j] == bucket[j - 1]): 
                    continue
                bucket[j]+=cookies[i]
                back(i+1)
                bucket[j]-=cookies[i]
        back(0)
        return self.minn