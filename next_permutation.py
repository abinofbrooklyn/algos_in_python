from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums)-1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            self.swap(nums,i,j)
        self.reverse(nums,i+1)
        return nums

    def reverse(self,nums,start):
        left = start
        right = len(nums)-1
        while left < right:
            self.swap(nums,left,right)
            left += 1
            right -= 1

    def swap(self,nums,i,j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


s = Solution()
print(s.nextPermutation([1,2,3]))
print(s.nextPermutation([3,2,1]))
print(s.nextPermutation([1,1,5]))
