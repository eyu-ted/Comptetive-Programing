class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic=Counter(nums1)
        ans=[]
        for n in nums2:
            if n in dic and dic[n]>0:
                ans.append(n)
                dic[n]-=1
        return ans
        
        