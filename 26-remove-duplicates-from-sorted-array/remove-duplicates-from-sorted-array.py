class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l=0
        # seen = set()
        for r in range(1,len(nums)):
            # if nums[r] not in seen:
            #     nums[l] = nums[r]
            #     l+=1
            # seen.add(nums[r])

            if nums[r] != nums[l]:
                l+=1
                nums[l] = nums[r]


        return l+1
            
        