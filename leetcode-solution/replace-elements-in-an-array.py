class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic={n:i for i,n in enumerate(nums)}
        for operation in operations:
            index=dic[operation[0]]
            nums[index]=operation[1]
            dic[operation[1]]=index
        return nums
        