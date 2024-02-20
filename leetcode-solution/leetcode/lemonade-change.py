class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        for n in bills:
            if n==5:
                five+=1
            elif n==10:
                if five >0:
                    five-=1
                elif five==0:
                    return False
                ten+=1
            elif n==20:
                if ten>=1 and five>=1:
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return  False
        return True
