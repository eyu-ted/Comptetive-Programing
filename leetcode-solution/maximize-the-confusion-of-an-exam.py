class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        dic=defaultdict(int)
        l=0
        maxx=-1
        for r in range(len(answerKey)):
            dic[answerKey[r]]+=1
            minn=min(dic["T"],dic["F"])
            while minn>k:
                dic[answerKey[l]]-=1
                minn=min(dic["T"],dic["F"])
                l+=1
            maxx=max(maxx,r-l+1)
        return maxx


        