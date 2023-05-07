from viajero import Viajero_frecuente
import csv

class Lista_viajero:
    
    def __init__(self):
        self.__viajeros = []
    
    def agregar_viajero(self, unViajero):
        self.__viajeros.append(unViajero)
        
    def get_viajero(self, num):
        return self.__viajeros[num]
    
    def mostrar_viajeros(self):
        for viajero in self.__viajeros:
            viajero.mostrar_datos()
    
    def buscar_viajero(self, numero:int):
        indice=0
        return_value = -1
        flag = False
        while not flag and indice < len(self.__viajeros):
            if self.__viajeros[indice].get_numero() == numero:
                flag = True
                return_value = indice
            else:
                indice+=1
        return return_value

    def test_lista_viajero(self):
        archivo=open('viajeros.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            Viajero = Viajero_frecuente(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]))
            self.agregar_viajero(Viajero)