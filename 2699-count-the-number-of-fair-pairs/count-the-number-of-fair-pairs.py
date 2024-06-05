class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def helper(val):
            
            l, r, count = 0, len(nums) - 1, 0

            while l <= r:
                tot = nums[l] + nums[r]
                if tot <= val:
                    l += 1
                    count += r - l + 1
                    
                else:
                    r-=1
            return count
        
        ans = helper(upper) - helper(lower -1)
        return ans