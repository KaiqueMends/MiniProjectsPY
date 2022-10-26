from cordenadaClass import cordenada
from quadranteClass import quadrante
from Menu import menu


def testGetQuadrant():
    # Arrange / Setup
    x = 5
    y = 10
    cordenadas = cordenada(x, y)
    Aquadrante = quadrante(cordenadas)

    # Act / Action
    result = Aquadrante.get_quadrante()
    
    # Assert
    assert result == "Primeiro Quadrante"

def testValidaCord():
    # Arrange / Setup
    x = 5
    y = 10
    cordenadas = cordenada(x, y)
    menu_user = menu()

    # Act / Action
    result = menu_user.validaCordenada(cordenadas)

    # Assert
    assert result == True
  