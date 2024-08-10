class rectangulo:
    def __init__(self, b,h):
        self.b = b
        self.h = h

    def cal_perimetro(self):
        perimetro = 2*(self.b + self.h)
        print("Perimetro:",perimetro)

    def cal_area(self):
        area = self.b * self.h
        print("Altura:",area)

    def comparativo(self):
        if self.b == self.h:
            print("Es un cuadrado")
        else:
            print("Es un rectangulo")
    
figura = rectangulo(8,14)
figura.cal_perimetro()
figura.cal_area()
figura.comparativo()