class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        dic = defaultdict(int)

        longest = 0
        sett = set(nums)

        for num in nums:
            x = num
            while x in sett:
                sett.remove(x)
                x += 1
            dic[num] = dic[x] + (x-num)
            longest = max(longest, dic[num])

        return longest 