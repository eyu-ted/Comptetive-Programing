class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """


        mid = m -1
        last = m+n -1

        right = n -1

        while right >-1:

            if mid >-1 and  nums2[right] < nums1[mid]:
                nums1[last] = nums1[mid]
                mid -=1
            else:
                nums1[last] = nums2[right]
                right-=1
            last -=1
