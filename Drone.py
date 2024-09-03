class Drone:
    def __init__(self, autonomia_maxima):
        self.autonomia_maxima = autonomia_maxima

    def calcular_distancia_total(self, caminho, distancias):
        return distancias[caminho[-1]]

    def verificar_viabilidade(self, caminho, distancias):
        distancia_total = self.calcular_distancia_total(caminho, distancias)
        distancia_retorno = distancia_total * 2  # ida e volta
        if distancia_retorno > self.autonomia_maxima:
            return False, f"Rota inviável: distância total de {distancia_retorno} metros excede a autonomia do drone ({self.autonomia_maxima} metros)."
        return True, distancia_total