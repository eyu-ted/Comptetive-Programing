class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def back_tracking(start,path):
            if len(path) == k:
                ans.append(path[:])
                return 
            if start>n:
                return 
            path.append(start)
            back_tracking(start+1,path)


            path.pop()
            back_tracking(start+1,path)

            
        back_tracking(1,[])
        return ans
            



            
        