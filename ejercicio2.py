class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def calcular_bono(self):
        return 0  # Base sin bono

class Gerente(Empleado):
    def calcular_bono(self):
        return self.salario * 0.20  # 20% de bono

class Tecnico(Empleado):
    def calcular_bono(self):
        return self.salario * 0.10  # 10% de bono