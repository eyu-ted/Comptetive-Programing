class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        maxx = max(nums)
        minn = 1
    

        def isPossible(n):
            summ = 0
            for num in nums:
                summ += ceil(num/n)
            
            return threshold >= summ


        while maxx >= minn:

            mid = (maxx+minn)//2


            if isPossible(mid):
                maxx = mid -1
            else:
                minn = mid + 1
            

        return minn
            
        