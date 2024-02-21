class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        c=0
        if target==1:
            return 0
        if maxDoubles==0:
            return target-1
        else:
            carry=0
            for i in range(maxDoubles):
                if target%2!=0:
                    carry+=1
                    target-=1
                target = target // 2
                c+=1
                if target==1:
                    break
            return c+carry+target-1

                    
                    
            

                
            return

        