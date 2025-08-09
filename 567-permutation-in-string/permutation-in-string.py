class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = Counter(s1)
        window = len(s1)

        l=0
        dic = defaultdict(int)
        for r in range(len(s2)):

            if r-l+1 > window:
                dic[s2[l]] -= 1
                if dic[s2[l]] ==0:
                    del dic[s2[l]]
                l+=1
            dic[s2[r]] += 1
            # print(r, dic,dic1)
            if dic == dic1:
                return True
        return False

        