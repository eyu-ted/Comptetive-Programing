class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        
        dic=defaultdict(int)
        ans=0
        for n in answers:
            if dic[n]==0:
                ans+= (1+n)
            else:
                if dic[n]>n:
                    ans+=(1+n)
                    dic[n]=0
            dic[n]+=1

        return ans


        