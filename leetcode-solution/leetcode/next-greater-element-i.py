class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        stack = []
        dic = { n:i for i,n in enumerate(nums1) }
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and stack[-1] < curr:
                ans[ dic[ stack[-1] ] ] = curr
                stack.pop()


            if curr in dic:
                stack.append( nums2[i] )
        return ans
        
        