class Solution:
    def numSquares(self, n: int) -> int:
        perfect = []

        for i in range(1,int(((n**0.5)//1)+1)):
            perfect.append(i**2)
        print(perfect)
        d = deque([(n,0)])
     

        visited = set()
        visited.add(n)

        while d:
            # print(d)
            summ,count = d.popleft()
            
            for per in perfect:
                new_sum = summ-per

                if new_sum == 0:
                    return count + 1

                if new_sum > 0 and new_sum not in visited:
                    d.append((new_sum, count+1))
                    visited.add(new_sum)
        return n


