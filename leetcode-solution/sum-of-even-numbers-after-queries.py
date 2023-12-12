class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total=0
        ans=[]
        for n in nums:
            if n%2==0:
                total+=n
        for query in queries:
            if nums[query[1]]%2!=0 and query[0]%2 !=0:
                total+=nums[query[1]]+query[0]
            elif  nums[query[1]]%2==0 and query[0]%2 ==0:
                total+=query[0]
            elif  nums[query[1]]%2==0 and query[0]%2 !=0:
                total-= nums[query[1]]
            
            ans.append(total)
            nums[query[1]]+=query[0]

            
            
        return ans
