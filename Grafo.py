class Grafo:
    def __init__(self, grafo):
        self.grafo = grafo

    def dijkstra(self, inicio):
        import heapq
        distancias = {v: float('inf') for v in self.grafo}
        distancias[inicio] = 0
        predecessores = {v: None for v in self.grafo}
        pq = [(0, inicio)]

        while pq:
            (distancia_atual, vertice_atual) = heapq.heappop(pq)

            if distancia_atual > distancias[vertice_atual]:
                continue

            for vizinho, peso in self.grafo[vertice_atual].items():
                distancia = distancia_atual + peso

                if distancia < distancias[vizinho]:
                    distancias[vizinho] = distancia
                    predecessores[vizinho] = vertice_atual
                    heapq.heappush(pq, (distancia, vizinho))

        return distancias, predecessores

    def reconstruir_caminho(self, predecessores, inicio, fim):
        caminho = []
        atual = fim
        while atual is not None:
            caminho.append(atual)
            atual = predecessores[atual]
        caminho.reverse()
        return caminho