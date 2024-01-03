class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while r>l:
            total=numbers[l]+numbers[r]
            if target>total:
                l+=1
            elif target<total:
                r-=1
            else:
                return [l+1,r+1]