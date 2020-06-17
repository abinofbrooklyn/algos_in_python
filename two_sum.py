def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff not in hash:
            hash[num] = i
        else:
            return [hash[diff], i]  
