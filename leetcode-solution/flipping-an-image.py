class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i]=image[i][::-1]
        for nums in image:
            for i in range(len(nums)):
                if nums[i]==1:
                    nums[i]=0
                else:
                    nums[i]=1
        return image
        