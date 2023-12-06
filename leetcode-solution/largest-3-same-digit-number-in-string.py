class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res=[]
        for i in range(len(num)-2):
            tri=num[i:i+3]
            if tri[0]==tri[1]==tri[2]:
                res.append(tri)
        return max(res) if res!=[] else ""

        
        
            


        