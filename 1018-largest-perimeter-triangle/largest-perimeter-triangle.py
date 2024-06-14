class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        res=[]
        for i in range(len(nums)-2):
            tri=nums[i:i+3]
            if tri[0]+tri[1]>tri[2]:
                res.append(sum(tri))
        return max(res) if res!=[] else 0
            

            
            

        