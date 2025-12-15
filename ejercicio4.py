class Vehiculo:
    def mover(self):
        print("El vehículo se está moviendo.")

class Carro(Vehiculo):
    def mover(self):
        print("El carro avanza por la carretera usando motor.")

class Bicicleta(Vehiculo):
    def mover(self):
        print("La bicicleta avanza pedaleando.")