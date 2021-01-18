class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        max_val, sum_val = 0, 0
        for num in nums:
            max_val = max(num, max_val)
            sum_val += num
        if m == 1:
            return sum_val

        left, right = max_val, sum_val
        while left <= right:
            mid = (left + right) // 2
            if self.is_valid(nums, mid, m):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def is_valid(self, nums, target, m):
        count, total = 1, 0
        for num in nums:
            total += num:
            if total > target:
                total = num
                count += 1
                if count > m:
                    return False
        return True 
