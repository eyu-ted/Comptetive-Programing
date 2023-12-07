class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      s=set()
      for r in range(len(ranges)):
        for x in range(ranges[r][0],ranges[r][1]+1):
          s.add(x)
      check=set()
      for x in range(left,right+1):
        check.add(x)
      return (check <= s)

        


        