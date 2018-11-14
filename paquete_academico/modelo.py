class Persona(object):
    def __init__(self):

        self.nombre = ""
        self.apellido = ""
        self.pais = Pais("", "")

    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_apellido(self, ape):
        self.apellido = ape

    def obtener_apellido(self):
        return self.apellido

    def agregar_pais(self, p):
        self.pais = p

    def obtener_pais(self):
        return self.pais.presentar_Pais()


class Pais(object):
    def __init__(self, nombre, capital):
        self.nombre = nombre
        self.capital = capital

    def agregar_nombre_p(self, nombre):
        self.nombre = nombre

    def agregar_capital(self, capital):
        self.capital = capital

    def obtener_nombre_p(self):
        return self.nombre

    def obtener_capital(self):
        return self.capital

    def presentar_Pais(self):
        cadena = "Pais - %s - Capital - %s\n" % (self.obtener_nombre_p(), self.obtener_capital())
        return cadena

class Estudiante(Persona):
    def __init__(self):
        super(Estudiante, self).__init__()
        self.codigo = 0

    #Métodos gets y sets de las variables
    def agregar_codigo(self, co):
        self.codigo = co

    def obtener_codigo(self):
        return self.codigo

class Estudiante_Presencial(Estudiante):
    def __init__(self):
        super(Estudiante_Presencial, self).__init__()
        self.num_creditos = 0
        self.ciclo = 0

    def agregar_num_credito(self, nc):
        self.num_creditos = nc

    def obtener_num_creditos(self):
        return self.num_creditos

    def agregar_ciclo(self, ci):
        self.ciclo = ci

    def obtener_ciclo(self):
        return self.ciclo
    #Metodo para presentae
    def presentar_datos(self):
        cadena = "DATOS:\nNombres: %s %s\nCodigo: %d\nPocedencia: %s\nNumero de creditos: %d\nCiclo: %d" % (
                 self.obtener_nombre(), self.obtener_apellido(), self.obtener_codigo(), self.obtener_pais(),
                 self.obtener_num_creditos(), self.obtener_ciclo())
        return cadena


class Estudiante_Distancia(Estudiante):
    #Metodo para declarar variables
    def __init__(self):
        super(Estudiante_Distancia, self).__init__()
        self.num_materias = 0
        self. modulo = 0
    #Metodos gets y sets
    def agregar_num_materias(self, nm):
        self.num_materias = nm

    def obtener_num_materias(self):
        return self.num_materias

    def agregar_modulo(self, mo):
        self.modulo = mo

    def obtener_modulo(self):
        return self.modulo

    # Presentacion
    def presentar_datos(self):
        cadena = "DATOS:\nNombres: %s %s\nCodigo: %d\nPocedencia: %s\nNumero de materias: %d\nModulo: %d" % (
                 self.obtener_nombre(), self.obtener_apellido(), self.obtener_codigo(), self.obtener_pais(),
                 self.obtener_num_materias(), self.obtener_modulo())
        return cadena