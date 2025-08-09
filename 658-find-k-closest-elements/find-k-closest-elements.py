class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        diffrence = []

        for num in arr :
            diffrence.append(abs(num-x))
        
        r = len(arr)-1
       
        summ = sum(arr[len(arr)-k:])
        minn = summ
        ran = (len(arr)-k,r)
        
        for l in range(len(arr)-k-1,-1,-1):
            summ+=diffrence[l]
            summ -= diffrence[r]
            r-=1
            if minn >= summ:
                ran = (l,r)
                minn = summ
            
            
  
        return arr[ran[0]:ran[1]+1]


