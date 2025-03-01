class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = defaultdict(int)

        def summ(num):
            result = 0

            while num:
                result += num % 10
                num //= 10
            
            return result
        maxx = -1

        for i in range(len(nums)):
            x = summ(nums[i])
            if x in dic:
                maxx = max(maxx, nums[i] + nums[dic[x]])

            if x in dic:
                if nums[dic[x]] < nums[i]:
                    dic[x] = i  
            else:
                dic[x] = i
        return maxx