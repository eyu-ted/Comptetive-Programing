class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        winsize=len(s1)
        l=0
        dicount=Counter(s1)
        dic=defaultdict(int)
        for r in range(len(s2)):
            if r-l==winsize:
                dic[s2[l]]-=1
                if dic[s2[l]]==0:
                    dic.pop(s2[l])
                l+=1
            dic[s2[r]]+=1
            if dicount==dic:
                return True
        return False


        