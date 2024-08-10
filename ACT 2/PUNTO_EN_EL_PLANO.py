class punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def mostrar(self):
        print("X:",self.x, "Y:",self.y)
        

    def mover(self, mx,my):
        self.x = mx
        self.y = my

    def calcular_distancia(self, p2):
        dx = p2.x - self.x
        dy = p2.y - self.y
        distancia = (dx**2 +dy**2)**0.5
        return distancia



coordenadas = punto(6,7)
coordenadas.mostrar()
coordenadas.mover(8,14)
coordenadas.mostrar()

punto2 = punto(15, 21)
distancia = coordenadas.calcular_distancia(punto2)
print("La distancia es:", distancia)


