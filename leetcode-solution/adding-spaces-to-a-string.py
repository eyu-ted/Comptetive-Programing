class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=""
        j=0
        i=0
        while i <len(s):
          if j< len(spaces) and spaces[j]==i:
            ans+=" "
            j+=1
          else:
            ans+=s[i]
            i+=1
        return ans
        

        