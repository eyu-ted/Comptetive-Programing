class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xy = 0
        for n in nums:
            xy ^= n
        
        xy = xy & (-xy)

        ans = [0,0]

        for num in nums:
            if xy &num:
                ans[0]^=num
            else:
                ans[1]^=num
        return ans
        