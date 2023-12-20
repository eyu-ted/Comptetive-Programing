class Solution:
    def plusOne(self, lis: List[int]) -> List[int]:
        # st=""
        # for c in lis:
        #     st+=str(c)
        # ans=int(st)+1
        # ans=list(str(ans))
        # for i in range(len(ans)):
        #     ans[i]=int(ans[i])
        # return ans
        m=len(lis)-1
        num=0
        for i in range(len(lis)):
            num+=lis[i]*(10**m)
            m-=1
        num+=1
        ans=[]
        while num:
            rem=num%10
            ans.append(rem)
            num=num//10
        return ans[::-1]


            
        