from Menu import menu
from quadranteClass import quadrante

menu_user = menu()

while menu_user.show_menu():
    cordenadas = menu_user.cordenadas

    AQuadrante = quadrante(cordenadas)
    print(f"{AQuadrante.get_quadrante()}")

