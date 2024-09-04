class Solution:
    def findNthDigit(self, n: int) -> int:

        size = 1
        digit = 9

        start = 1

        while digit*size < n:

            n -= (size*digit)

            size += 1
            digit *= 10
            start *=10

        target = start+(n-1)//size 
        pos = n%size

        if pos ==0:
            return target%10
        else:
            for _ in range(size - pos):
                target //= 10
        return target % 10



        
        