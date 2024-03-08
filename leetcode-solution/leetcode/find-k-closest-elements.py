class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        r=len(arr)-k
        while r>l:
            mid = (l+r)//2

            if x - arr[mid] > arr[k+mid]-x:
                l = mid+1
            else:
                r=mid
        return arr[l:l+k]
        