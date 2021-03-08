class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        idx1 = m-1
        idx2 = n-1
        merge_idx = m + n - 1

        while merge_idx >= 0:
            if idx2 >= 0 and (m == 0 or nums2[idx2] >= nums[idx1]):
                nums1[merge_idx] = nums2[idx2]
                idx2 -= 1
            elif idx2 > -1 and num1[idx1] > num2[idx2]:
                nums1[merge_idx], nums1[idx1] = nums1[idx1], nums1[merge_idx]

                if idx1:
                    idx1 -= 1
            merge_idx -=1

            if idx2 > -1:
                for i in range(idx2+1):
                    nums1[i] = nums2[i]
