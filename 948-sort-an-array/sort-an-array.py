class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def sortt(left, right):
            merged =[]

            l=0
            r=0
            while l<len(left) and r<len(right):
                if left[l]>right[r]:
                    merged.append(right[r])
                    r+=1
                else:
                    merged.append(left[l])
                    l+=1
            while l<len(left):
                merged.append(left[l])
                l+=1
            while r<len(right):
                merged.append(right[r])
                r+=1
            return merged
        
        def merge_sort(nums):
            if len(nums) <=1:
                return nums
            left = merge_sort(nums[:len(nums)//2])
            right = merge_sort(nums[len(nums)//2:])
    
            return sortt(left,right)
        
        return merge_sort(nums)


        