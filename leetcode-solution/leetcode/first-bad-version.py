# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:


        l=1
        r=n
   
        ans = 0
        while l<=r:

            mid = (l+r)//2


            if isBadVersion(mid) == True and isBadVersion(mid-1) == False:
                return mid
            elif isBadVersion(mid) == True :
                r = mid-1
            elif  isBadVersion(mid) != True:
                l = mid+1

                


        


        
        