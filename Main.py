# Dados do drone
from Drone import Drone
from Grafo import Grafo

autonomia_maxima = 10500  # Em metros (10,5 km)

# Exemplo de representação de grafo
grafo_dados = {
    'heliporto': {'zona1': 300, 'zona2': 200, 'destino': 950},
    'zona1': {'heliporto': 300, 'zona2': 1200, 'destino': 600},
    'zona2': {'heliporto': 200, 'zona1': 1200, 'destino': 500},
    'destino': {'heliporto': 950, 'zona2': 500, 'zona1': 600},
}

grafo = Grafo(grafo_dados)
drone = Drone(autonomia_maxima)

print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
distancias, predecessores = grafo.dijkstra('heliporto')
caminho = grafo.reconstruir_caminho(predecessores, 'heliporto', 'destino')
print("Distâncias:", distancias)
print("Caminho de Heliporto para Destino:", caminho)
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------")
# Verificando se a autonomia é suficiente para a rota de ida e volta
viavel, resultado = drone.verificar_viabilidade(caminho, distancias)

if viavel:
    print(f"Caminho de Heliporto para Destino: {caminho}")
    print(f"Distância Total (ida): {resultado} metros")
    print(f"Distância Total (volta até o heliporto): {resultado} metros")
    print(f"Distância Total (ida e volta): {resultado * 2} metros")
else:
    print(resultado + " Não é possivel realizar a rota")