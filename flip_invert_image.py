class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for image in A:
            image.reverse()
            for i in range(len(image)):
                image[i] ^= 1
        return A
