from manejador_viajero import Lista_viajero
from viajero import Viajero_frecuente
from menu import Menu

if __name__ == '__main__':
    menu = Menu()
    lista = Lista_viajero()
    lista.test_lista_viajero()
    lista.mostrar_viajeros()
    num = int(input('Ingrese número de viajero'))
    pos = lista.buscar_viajero(num)
    viajero = lista.get_viajero(pos)
    viajero.mostrar_datos()
    menu.menu(viajero)