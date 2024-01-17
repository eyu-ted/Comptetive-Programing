class Solution:
    def smallestNumber(self, num: int) -> int:
        if num==0:
            return 0
        elif num>0:
            num=list(str(num))
            num.sort()
            if num[0]=="0":
                l=0
                r=0
                while r<len(num):
                    if num[r]!="0":
                        num[r],num[l]=num[l],num[r]
                        break
                    r+=1
            return int("".join(num))
        else:
            sl=list(str(num))
            sl=sl[1:]
            sl.sort(reverse=True)
            return -1*(int("".join(sl)))
        
        