class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(num):
            half = len(num)//2
            if half:
                left,right = merge_sort(num[:half]),merge_sort(num[half:])
           
                for i in range(len(num))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        ans[left[-1][0]] += len(right)
                        num[i] = left.pop()
                    else:
                        num[i] = right.pop()
            return num
        
        ans = [0]*len(nums)
        lis = []

        for i,num in enumerate(nums):
            lis.append((i,num))
    
        merge_sort(lis)
        return ans
            
            