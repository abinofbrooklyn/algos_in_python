class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end, largest = 0, len(height)-1, 0
        prev_start = prev_end = 0

        while start != end:
            if height[start] < prev_start:
                start += 1
                continue
            if height[end] < prev_end:
                end -= 1
                continue

            area = min(height[start], height[end]) * (end - start)

            if largest < area:
                largest = area

            if height[start] < height[end]:
                prev_start = start
                start += 1
            else:
                prev_end = end
                end -= 1

        return largest
