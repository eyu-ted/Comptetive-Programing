class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dic = defaultdict(int)

        currn_sum = 0
        dic[0] = 1
        count = 0

        for num in nums :
            currn_sum += num

            count += dic[currn_sum - k]

            dic[currn_sum] += 1

        return count 

            

