class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        seen = set()
        nums.sort()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left = j+1
                right = len(nums)-1
                
                while left < right:
                    summ = nums[i] + nums[j] + nums[left] + nums[right]
                    if summ == target and (nums[i],nums[j],nums[left],nums[right]) not in seen:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        seen.add((nums[i],nums[j],nums[left],nums[right]))
                    elif summ > target:
                        right-=1
                    else:
                        left+=1
        

        return result 
