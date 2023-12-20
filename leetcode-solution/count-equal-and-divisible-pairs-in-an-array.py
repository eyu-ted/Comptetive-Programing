class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        dic={}
        ans=0
        for i in range(len(nums)):
            if nums[i] in dic:
                for j in dic[nums[i]]:
                    if j*i%k==0:
                        ans+=1
                dic[nums[i]].append(i)
            else:
                dic[nums[i]]=[i]
        return ans
                    

        