def maxSubarray(self, nums: List[int]) -> int:
    return self.helper(nums, 0, len(nums) - 1)

def helper(self, nums, left, right):
    if left == right:
        return nums[left]

    middle = (left + right) // 2

    left_sum = self.helper(nums, left, middle)
    right_sum = self.helper(nums, middle + 1, right)
    cross_sum = self.cross_sum(nums, left, right, middle)

    return max(left_sum, right_sum, cross_sum)

def cross_sum(self, nums, left, right, middle):
    if left == right:
        return nums[left]

    left_sum = float(-inf)
    curr_sum = 0
    for i in range(middle,left-1,-1):
        curr_sum += nums[i]
        left_sum = max(curr_sum, left_sum)

    right_sum = float(-inf)
    curr_sum = 0
    for i in range(middle+1, right+1):
        curr_sum += nums[i]
        right_sum = max(curr_sum, right_sum)

    return left_sum + right_sum
