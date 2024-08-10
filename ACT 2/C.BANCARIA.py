class cuentaBancaria():
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, deposito):
        if deposito >0:
            self.balance +=deposito
            print("El nuevo balance es:", self.balance)

    def retiros(self, ret):
        if ret >0:
            self.balance =self.balance-ret
            print("El nuevo balance es:", self.balance)

    def cuota_manejo(self,):
        cuota = self.balance*0.02
        print("El valor de la cuota de manejo es:",cuota)

    def mostrar_detalles(self):
        print("NUMERO DE CUENTA:",self.numero_cuenta, "PROPIETARIOS:",self.propietarios, "BALANCE ACTUAL:",self.balance )

bryan = cuentaBancaria(1033178569, 1, 3000000)
bryan.depositar(200)
bryan.retiros(400)
bryan.cuota_manejo()
bryan.mostrar_detalles()