class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic={}
        t=len(nums)//3
        res=[]
        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        for n in nums:
            if dic[n]>t and n not in res:
                res.append(n)
        return res

        
        