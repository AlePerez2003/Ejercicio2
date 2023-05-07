class Viajero_frecuente:
    __numero: int
    __dni: str
    __nombre: str
    __apellido: str
    __millasAcum: int
    
    def __init__(self, numero, dni, nombre, apellido, millas_acum):
        self.__numero = numero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = millas_acum
        
    def get_millas(self):
        return self.__millasAcum
    
    def acumular_millas(self, millas):
        self.__millasAcum+=millas
        return
    
    def verificar_millas(self, millas):
        if (self.__millasAcum >= millas):
            canjearmillas = True
        else:
            canjearmillas = False
        return canjearmillas
    
    def canjear_millas(self, millas):
        if (self.verificar_millas(millas)):
            self.__millasAcum-=millas
        else:
            print('Error de la Operacion: Millas insuficientes')
        return self.__millasAcum
    
    def get_numero(self):
        return self.__numero
    
    def mostrar_datos(self):
        print ('Datos del Viajero:')
        print ('Numero: {}'.format(self.__numero))
        print ('DNI:' + self.__dni)
        print ('Nombre y Apellido:' + self.__nombre , self.__apellido)
        print ('Millas Acumuladas: {}'.format(self.__millasAcum))
        print ('')