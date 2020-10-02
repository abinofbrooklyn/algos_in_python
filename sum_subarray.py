class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map = {}
        sums = 0
        count = 0
        map[0] = 1
        for idx in range(0,len(nums)):
            sums += nums[idx]
            if (sum-k) in map:
                count += map[sum-k]
            if sum in map:
                map[sum] += 1
            else:
                map[sum] = 1
        return count
