class Solution:
    def maxPower(self, s: str) -> int:
        count, max_count, previous = 0, 0, None

        for c in s:
            if c == previous:
                count += 1
            else:
                count = 1
                previous = c
        max_count = max(max_count, count)
    return max_count
