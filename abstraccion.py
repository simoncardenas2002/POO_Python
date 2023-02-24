class Lavadora:
    def __init__(self):
        pass

    def lavar(self,temperatura="caliente"):
        self._llenar_tanque(temperatura)
        self._añadir_jabon()
        self._proceso()
        self._centrifugar()

    def _llenar_tanque(self,temperatura):
        print(f"llenando el tanque con agua {temperatura}")

    def _añadir_jabon(self):
        print("Añadiendo jabon")

    def _proceso(self):
        print("lavando")

    def _centrifugar(self):
        print("Centrifugando la ropa")

if __name__ == '__main__':
  lavadora=Lavadora()
  lavadora.lavar()
  print("-"*20)
  