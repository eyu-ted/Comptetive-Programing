class Solution:
    def largestOddNumber(self, num: str) -> str:
      last_index=0
      flag=0
      for i,n in enumerate(num):
        if int(n)%2!=0:
          flag=1
          last_index=i
      return num[:last_index+1] if flag== 1 else ""
        


                
        