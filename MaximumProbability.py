import collections
import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges:List[List[int]], probaSuce: List[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src,dst = edges[i]
            adj[src].append([dst, probaSuce[i]])
            adj[dst].append([src, probaSuce[i]])

        
        pq = [(-1, start)]
        visitar = set()

        while pq:
            prob, cur = heapq.heappop(pq)
            visitar.add(cur)

            if cur == end:
                return prob*-1
            for nei,probaSuce in adj[cur]:
                if nei not in visitar:
                    heapq.heappush(pq,(prob*probaSuce,nei))
        
        return 0
