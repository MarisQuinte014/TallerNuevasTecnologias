class Banco: 

    def __init__(self, nombre, apellido, cedula, ciudad,cuenta, saldo): 
        self.nombre = nombre,
        self.apellido = apellido,
        self.cedula = cedula,
        self.ciudad = ciudad,
        self.cuenta = cuenta,
        self.saldo = saldo


    banco = {}

    def buscarSaldo(self):
        print(f'Su saldo es {self.saldo}')

    def agregarSaldo(self, saldo):
        self.saldo = self.saldo + saldo 

    def retirarSaldo(self, saldo):
        self.saldo = self.saldo - saldo