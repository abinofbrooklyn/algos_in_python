class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, [])
        return self.res

    def backtrack(nums, path):
        if not nums:
            return self.res.append(path)
        for i in range(len(nums)):
            self.backtrack(nums[:i]+nums[i+1:], path+[nums[i]])
