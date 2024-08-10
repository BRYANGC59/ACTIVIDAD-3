class circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def cal_area(self):
        area = 3.1416*self.radio**2
        print("Area:",area)
    
    def cal_perimetro(self):
        perimetro = 2*(3.1416*self.radio)
        print("Perimetro:",perimetro) 

figura = circulo(1,3)
figura.cal_area()
figura.cal_perimetro()