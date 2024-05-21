class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dic = {}

        for num in arr:
            diff = num + difference
            if num in dic:
                dic[diff] = dic[num]+1
            else:
                dic[diff] = 1
        return max(dic.values())

            

            

                
            
        