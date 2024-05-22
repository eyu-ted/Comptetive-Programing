class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def word(st):
            sett = set()

            for ch in st:
                sett.add(ch)
            
            return sett

        
        arr = []
        length = []

        for wrd in words:
            arr.append(word(wrd))
            length.append(len(wrd))
        

        maxx = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
       
                if len(arr[i] & arr[j]) ==0:
                    maxx= max(maxx,length[i]*length[j])

 
        return maxx


        