class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans=[]
        def swap(last):
            intial=0
            while last> intial:
                arr[last],arr[intial]=arr[intial],arr[last]
                last-=1
                intial+=1
        for i in range(len(arr)-1,-1,-1):
            maxx=i
            for j in range(i,-1,-1):
                if arr[j]>arr[maxx]:
                    maxx=j
            if maxx!=i:
                swap(maxx)
                swap(i)
                ans.append(maxx+1)
                ans.append(i+1)
        return ans

        