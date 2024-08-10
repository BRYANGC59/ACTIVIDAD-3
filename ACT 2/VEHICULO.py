class vehiculo:
    def __init__(self, velocidad_maxima, kilometros):
        self.velocidad_maxima = velocidad_maxima
        self.kilometros = kilometros

carro = vehiculo(220, 7000)
print(carro.velocidad_maxima, carro.kilometros)

