class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_product = [nums[0]]
        suffix_product = [nums[-1]] 

        for i in range(1,len(nums)):
            prefix_product.append(prefix_product[-1] * nums[i])
        
        for i in range(len(nums)-2,-1,-1):
            suffix_product.append(suffix_product[-1] * nums[i])
        
        suffix_product.reverse()
        
        result = []
        n = len(nums)
        for i in range(n):
            if i == 0:
                result.append(suffix_product[i+1])
            elif i == n-1:
                result.append(prefix_product[i-1])
            else:
                result.append(prefix_product[i-1] * suffix_product[i+1])



        return result

        