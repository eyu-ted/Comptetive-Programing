class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()

        def back(start , path):

            if path not in ans:
                ans.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                back(i+1,path)
                path.pop()
        back(0,[])
        return ans

        