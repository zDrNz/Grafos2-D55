import heapq
from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visitar = set()
        heapMin = [[grid[0][0], 0, 0]]
        direcao = [[0,1],[0,-1],[1,0],[-1,0]]

        visitar.add((0,0))
        while heapMin:
            t, l, c = heapq.heappop(heapMin)
            if l == N - 1 and c == N - 1:
                return t
            for dr, dc in direcao:
                neiL, neiC = l + dr, c + dc
                if (neiL<0 or neiC<0 or
                    neiL ==N or neiC == N or
                    (neiL, neiC) in visitar):
                    continue
                visitar.add((neiL,neiC))
                heapq.heappush(heapMin, [max(t,grid[neiL][neiC]), neiL, neiC])
