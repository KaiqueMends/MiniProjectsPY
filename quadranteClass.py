from cordenadaClass import cordenada

class quadrante:

    def __init__(self, cordenadas: cordenada) -> None:
        self.cordenadas = cordenadas

    def get_quadrante(self) -> str:
        
        cordenadaX = self.cordenadas.cordenadaX
        cordenadaY = self.cordenadas.cordenadaY

        if (cordenadaX > 0 and cordenadaY > 0):
            return "Primeiro Quadrante"
        elif (cordenadaX < 0 and cordenadaY > 0):
            return "Segundo Quadrante"
        elif (cordenadaX < 0 and cordenadaY < 0):
            return "Terceiro Quadrante"
        elif (cordenadaX > 0 and cordenadaY < 0):
            return "Quarto Quadrante"
        else:
            return ""
    

