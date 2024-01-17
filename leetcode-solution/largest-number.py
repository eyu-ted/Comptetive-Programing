class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        def compare(x,y):
            if x+y>y+x:
                return -1
            return 1
        nums=sorted(nums,key=cmp_to_key(compare))
        return str(int("".join(nums)))
        
        