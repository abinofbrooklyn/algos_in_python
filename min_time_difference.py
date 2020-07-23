class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        minDiff = float('inf')

        def timeDiff(t1,t2):
            t1hh, t1mm = t1.split(":")
            t2hh, t2mm = t2.split(":")
            hour_diff = (int(t2hh) - int(t1hh)) * 60
            min_diff = int(t2mm) - int(t1mm)
            return hour_diff + min_diff

        for i in range(1,len(timePoints)):
            t1 = timePoints[i-1]
            t2 = timePoints[i]
            minDiff = min(timeDiff(t1,t2), minDiff)
            last2 = (1440 + timeDiff(timePoints[-1], timePoints[0]))
            minDiff = min(last2, minDiff)

        return minDiff
