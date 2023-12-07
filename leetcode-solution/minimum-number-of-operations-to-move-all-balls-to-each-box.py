class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        record=[]
        ans=[]
        for i,n in enumerate(boxes):
            if n=="1":
                record.append(i)
        for i in range(len(boxes)):
            step=0
            for r in record:
                step+=abs(i-r)
            ans.append(step)
        return ans
                 

        