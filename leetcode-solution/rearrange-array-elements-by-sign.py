class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive=[]
        negative=[]
        res=[]
        for n in nums:
            if n>0:
                positive.append(n)
            else:
                negative.append(n)
        for i in range(len(nums)//2):
            res.append(positive[i])
            res.append(negative[i])
        return res

        