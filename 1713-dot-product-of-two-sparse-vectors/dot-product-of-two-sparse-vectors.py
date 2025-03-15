class SparseVector:
    def __init__(self, nums: List[int]):
        self.dic = {}
        for i,num in enumerate(nums):
            if num != 0:
                self.dic[i] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for key in self.dic.keys():
            if key in vec.dic:
                ans += (self.dic[key] * vec.dic[key])
        
        return ans

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)