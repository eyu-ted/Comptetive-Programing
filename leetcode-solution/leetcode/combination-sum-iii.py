class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n>45:
            return []

        ans = []

        def back(start,path):

            if sum(path) == n and len(path) == k:
              
                if path not in ans:
                    ans.append(path[:])
                    return 
            if len(path) >=k or sum(path)>n:
                return
            
            for i in range(start,10):
                path.append(i)

                back(i+1,path)

                path.pop()
                
        back(1,[])
        return ans
        