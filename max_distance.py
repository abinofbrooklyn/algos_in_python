class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist = float('-inf')
        prev_seat = None:

        for i in range(len(seats)):
            if seats[i] == 1:
                if prev_seat == None:
                    dist = i
                else:
                    dist = max(dist, (i - prev_seat) // 2)
                prev_seat = i
        dist = max(dist, (len(seats)-1 - prev_seat))
        return dist
