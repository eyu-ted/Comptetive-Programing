class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        op = []
        p = puma(nums, op)
        return p
def puma(a, op):
    if len(a) == 2:
        op.append(a)
        op.append(a[::-1])
        return op
    else:
        expo = []
        piku = a[0]
        op = puma(a[1:], op)
        for j in op:
            for i in range(0, len(j) + 1):
                k = j[:i] + [piku] + j[i:]
                expo.append(k)
        return expo