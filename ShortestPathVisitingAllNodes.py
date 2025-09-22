from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        n = len(graph)
        #nó atual, marcador de visitados, custo acumulado
        queue = deque((i, 1 << i, 0) for i in range(n))  
        visited = set((i, 1 << i) for i in range(n)) 

        # BFS para explorar todos
        while queue:
            node, mark, cost = queue.popleft()

            # Se todos os nós foram visitados
            if mark == (1 << n) - 1:
                return cost

            # Explorar os vizinhos
            for neighbor in graph[node]:
                next_mark = mark | (1 << neighbor)  # Atualiza o marcador de visitados
                if (neighbor, next_mark) not in visited:
                    visited.add((neighbor, next_mark))
                    queue.append((neighbor, next_mark, cost + 1))

        return -1  # Não alcançável para grafos conectados