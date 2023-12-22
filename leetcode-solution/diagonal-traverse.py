class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans=[]
        dic=defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                dic[i+j].append(mat[i][j])
        for key in dic.keys():
            if key%2!=0:
                for n in dic[key]:
                    ans.append(n)
            else:
                for i in range(len(dic[key])-1,-1,-1):
                    ans.append(dic[key][i])
        return ans




        