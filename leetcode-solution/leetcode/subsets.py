class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def back_tracking(start,path):

            ans.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                back_tracking(i+1,path)
                path.pop()
            
        back_tracking(0,[])
        return ans