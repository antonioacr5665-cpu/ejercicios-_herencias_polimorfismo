class Dispositivo:
    def encender(self):
        print("Dispositivo encendido.")

class Laptop(Dispositivo):
    def encender(self):
        print("Laptop iniciando sistema operativo...")

class Telefono(Dispositivo):
    def encender(self):
        print("Teléfono mostrando pantalla de inicio.")