class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        tip=max(arr)
        if arr[0]==tip or arr[-1]==tip or len(arr)<3:
            return False
        for i in range(len(arr)-1):
            if arr[i]==tip:
                break
            if  arr[i]>=arr[i+1]:
                return False
            
        for j in range(i,len(arr)-1,1):
            if  arr[j]<=arr[j+1]:
                return False

        return True

        

        