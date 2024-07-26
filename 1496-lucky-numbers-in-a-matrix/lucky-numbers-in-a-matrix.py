class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minn = []
        maxx =[float("-inf")]*len(matrix[0])

        

        for i in range(len(matrix)):
            x = float("inf")

            for j in range(len(matrix[0])):
                x = min(x,matrix[i][j])
                maxx[j] = max(maxx[j],matrix[i][j])
            
            
            minn.append(x)
        settmaxx = set(maxx)
        settminn = set(minn)

        ans = []
        for num in maxx:
            if num in settminn:
                ans.append(num)

        return ans
        