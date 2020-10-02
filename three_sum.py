class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)-2):
            res = self.two_sum(nums, i+1, -nums[i], res)
        return res

    def two_sum(self, nums, start, target, res):
        left, right = start, len(nums)-1
        while left < right:
            if nums[left] + nums[right] == target:
                res.add([nums[left], nums[right], -target])
                left += 1
                right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return res
