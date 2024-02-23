class Solution:
    def numberOfWays(self, s: str) -> int:
        left_zero_count = 0
        right_zero_count = s.count("0")
        left_one_count=0
        right_one_count=s.count("1")
        
        ways=0
        for i in range(len(s)):
            if s[i]=="1":
                ways += left_zero_count * right_zero_count
                left_one_count+=1
                right_one_count-=1

            else:
                ways += ( left_one_count ) * ( right_one_count )
                left_zero_count += 1
                right_zero_count -= 1
        return ways
        


