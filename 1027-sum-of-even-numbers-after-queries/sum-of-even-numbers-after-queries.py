class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total=0
        ans=[]
        for n in nums:
            if n%2==0:
                total+=n
        for val,index in queries:
            if nums[index]%2!=0 and val % 2 !=0:
                total+=nums[index]+val
            elif  nums[index]%2==0 and val % 2 ==0:
                total += val
            elif  nums[index] % 2 == 0 and val % 2 !=0:
                total-= nums[index]
            
            ans.append(total)
            nums[index] += val
            
        return ans
