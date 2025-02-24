class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dictionary = defaultdict(int)
        set_nums = set(nums)

        longest = float("-inf")

        for num in nums:
            x = num
            while x in set_nums:
                set_nums.remove(x) 
                x+=1
            
            dictionary[num] = dictionary[x] + (x-num)
            longest = max(longest, dictionary[num])
        return longest
