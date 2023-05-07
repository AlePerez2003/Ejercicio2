from viajero import Viajero_frecuente
from manejador_viajero import Lista_viajero

class Menu:
    __cod = int
    
    def __init__(self, cod = 0):
        self.__cod = cod

    def mostrar_menu(self):
        print ('1: Consultar Millas')
        print ('2: Acumular Millas')
        print ('3: Consumir Millas')
        print ('0: Finalizar Operación')
        
    def menu(self, viajero):
        self.mostrar_menu()
        self.__cod = int(input('Ingrese el código'))
        while self.__cod != 0:
            if self.__cod == 1:
                self.opcion1(viajero)
            elif self.__cod == 2:
                self.opcion2(viajero)
            elif self.__cod == 3:
                self.opcion3(viajero)
            else:
                print ('Codigo incorrecto, ingrese de nuevo')
            self.mostrar_menu()
            self.__cod = int(input("Ingrese el código"))
        
        
    def opcion1(self, viajero):
        print("El total de millas es:{}".format(viajero.get_millas()))
        
    def opcion2(self, viajero:Viajero_frecuente):
        viajero.acumular_millas(int(input('Ingrese cantidad de Millas')))
    
    def opcion3(self, viajero):
        viajero.canjear_millas(int(input('Ingrese millas a consumir')))