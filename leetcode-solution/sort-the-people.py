class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic={}
        for i in range(len(heights)):
            dic[heights[i]]=names[i]
        for i in range(len(heights)-1,-1,-1):
            for j in range(i):
                if heights[j]<heights[j+1]:
                    temp=heights[j]
                    heights[j]=heights[j+1]
                    heights[j+1]=temp
        ans=[]
        for n in heights:
            ans.append(dic[n])
        return ans
                


        