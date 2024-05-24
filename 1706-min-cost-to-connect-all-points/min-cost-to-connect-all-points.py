class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        par = [i for i in range(len(points))]
        rank = [1 for i in range(len(points))]
        def find(x):
            t= par[x]
            while t != par[t]:
                par[t] = par[par[t]]
                t=par[t]
            return t

        def union(x,y):
            parent1 = find(x)
            parent2 = find(y)

            if parent1!= parent2:
                if rank[parent1] > rank[parent2]:
                    par[parent2] = parent1
                    rank[parent1] += rank[parent2]
                else:
                    par[parent1] = parent2
                    rank[parent2] += rank[parent1]
        
        lis = []
        def cal(a,b,c,d):
            return abs(a-b) + abs(c-d)
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                distance = cal(points[i][0],points[j][0],points[i][1],points[j][1])
                lis.append([distance,i,j])
        
        lis.sort()
        ans =0
        c=0

        for arr in lis:
            dis , p1 ,p2 = arr
            parent1 = find(p1)
            parent2 = find(p2)
            if parent1 != parent2:
                ans+=dis
                union(parent1, parent2)
                c+=1
                if c == len(points):
                    break
        return ans
 