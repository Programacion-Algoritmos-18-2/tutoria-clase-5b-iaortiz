from paquete_academico.modelo import *
ed = Estudiante_Distancia()			 # Objeto de tipo estudiante a ditancia
ed.agregar_nombre("Jenny")			 # Agregamos nombre
ed.agregar_apellido("Diaz")			 # Agregamos apellido
ed.agregar_codigo(50078)			 # Agregamos codigo
ed.agregar_num_materias(7)          # Agregamos el numero de  materias
ed.agregar_modulo(4)                # Agregamos el modulo
p = Pais("Ecuador", "Quito")        # Agregamos el pais y capital en una variable de tipo pais
ed.agregar_pais(p)                  # agregamos los datos al objeto de tipo estudiante
print(ed.presentar_datos())         # Presentacion
