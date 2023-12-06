class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        x=0
        y=n
        for _ in range(n):
            ans.append(nums[x])
            ans.append(nums[y])
            x+=1
            y+=1
        return ans

        