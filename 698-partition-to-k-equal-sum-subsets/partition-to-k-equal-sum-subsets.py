class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        used = [0] * len(nums)

        def backtrack(i):
            if  i >= len(nums):
                return True
            
            for j in range(k):
                if used[j] + nums[i] <= target:
                    used[j] += nums[i]

                    if backtrack(i+1):
                        return True

                    used[j] -= nums[i]
                    if not used[j]:
                        break

            return False

        return backtrack(0) 
        
        