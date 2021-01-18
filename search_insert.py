class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target or (nums[mid] > target and (mid == 0 or nums[mid - 1] < target)):
                return mid
            if mid == len(nums) - 1 and nums[mid] < target:
                return mid + 1
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
 
