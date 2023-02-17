class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print("Caminando")

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print("Pedaleando en la bici")

def main():
    persona= Persona("Simon")
    persona.avanza()

    ciclista=Ciclista("Pedro")
    ciclista.avanza()

if __name__ == '__main__':
    main()


