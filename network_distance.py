from collections import deafaultdict
from heapq import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.deafaultdict(list)

        for edges in times:
            node, target, time = edge[0], edge[1], edge[2]
            graph[node].append((time, target))

        dist = {}
        pq = [(0, K)]

        while pq:
            time, node = heappq.heappop(pq)
            if node not in dist:
                dist[node] = time
                for neighbor_time, neighbor in graph[node]:
                    if neighbor not in dist:
                        heapq.heappush(pq, (neighbor_time + time, neighbor))

        res = max(dist.values())
        return res if N == len(dist) else -1
