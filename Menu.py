from operator import truediv
from cordenadaClass import cordenada

class menu:
    def __init__(self) -> None:
        pass

    def setarCordenadas(self) -> cordenada:
        cordenadaX = int(input("Qual a cordenada de X? "))
        cordenadaY = int(input("Qual a cordenada de Y? "))
        self.cordenadas = cordenada(cordenadaX, cordenadaY)
        return self.cordenadas

    def validaCordenada(self, Acordenada: cordenada) -> bool:
        if (Acordenada.cordenadaX == 0 or Acordenada.cordenadaY == 0):
            return False
        else:
            return True

    def show_menu(self) -> bool:
        self.setarCordenadas()
        return self.validaCordenada(self.cordenadas)        

    



