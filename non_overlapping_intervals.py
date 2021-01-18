class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval:interval[1])
        count, prev = 0, float('-inf')

        for interval in intervals:
            if interval[0] > prev:
                prev = interval[1]
            else:
                count += 1
        return count 
