class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        sett = set(position)
        def check(l):
            last = position[0]
            c=1
            for i in range(len(position)):
                if position[i] - last >= l:
                    last= position[i]
                    c+=1

            
            if c >=m:

                return True

            return False

        position.sort()
        l=1
        r = position[-1]*2

        while r>l:
            midd = (r+l)//2
            if check(midd):
                l=midd+1
            else:
                r=midd
        return l-1
