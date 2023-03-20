###############################################################################
#                                                                             #
#                         EJERCICIO INTEGRADOR PYTHON                         #
#                                                                             #
###############################################################################

###############################################################################
#                                   PUNTO 1                                   #
###############################################################################

# a=120
# b=30

# def mcd(a,b):
#     if b==0:
#         return a
#     else:
#         return mcd(b,a%b)
    
# mcd=mcd(10,30)

# print(mcd)

###############################################################################
#                                   PUNTO 2                                   #
###############################################################################

# a=15
# b=30

# def mcm(a,b):
#     def mcd(a,b):
#         if b==0:
#             return a
#         else:
#             return mcd(b,a%b)
#     return (a*b)//mcd(a,b)

# mcm=mcm(a,b)
# print(mcm)

###############################################################################
#                                   PUNTO 3                                   #
###############################################################################

# def diccionario(a):
#     palabras = a.split()
#     cont = {}
#     for palabra in palabras:
#         if palabra in cont:
#             cont[palabra]=cont[palabra]+1
#         else:
#             cont[palabra]=1
#     return cont

# dicc=diccionario("Esto es una prueba. Repito es una prueba")
# print(dicc)

###############################################################################
#                                   PUNTO 4                                   #
###############################################################################

# def diccionario(a):
#     palabras = a.split()
#     cont = {}
#     for palabra in palabras:
#         if palabra in cont:
#             cont[palabra]=cont[palabra]+1
#         else:
#             cont[palabra]=1
#     return cont


# def tupla(dicc):
#     palabra=max(dicc, key=dicc.get)
#     cont=dicc[palabra]
#     return (palabra, cont)

# dicc=diccionario("Esto es una prueba. Repito es una prueba. Es prueba.")
# print(dicc)
# tup=tupla(dicc)
# print(tup)

###############################################################################
#                                   PUNTO 5                                   #
###############################################################################

# def get_int():
#     while True:
#         try:
#             num = int(input("Ingrese un número entero: "))
#             return num
#         except ValueError:
#             print("Por favor, ingrese un numero entero.")

# def get_int():
#     try:
#         num = int(input("Ingrese un número entero: "))
#         return num
#     except ValueError:
#         print("El valor ingresado no es un número entero válido. Intente nuevamente.")
#         return get_int()
    
###############################################################################
#                                   PUNTO 6                                   #
###############################################################################

# class Persona:
#     def __init__(self, nombre="", edad=0, dni="") -> None:
#         self.nombre = nombre
#         self.edad = edad
#         self.dni = dni

#     def get_nombre(self):
#         return self.nombre

#     def set_nombre(self, nombre):
#         self.nombre = nombre

#     def get_edad(self):
#         return self.edad

#     def set_edad(self, edad):
#         if edad >= 0:
#             self.edad = edad
#         else:
#             print("La edad debe ser un valor positivo.")

#     def get_dni(self):
#         return self.dni

#     def set_dni(self, dni):
#         if len(dni) == 8:
#             self.dni = dni
#         else:
#             print("El DNI debe tener 8 dígitos.")

#     def mostrar(self):
#         print("Nombre:", self.nombre)
#         print("Edad:", self.edad)
#         print("DNI:", self.dni)

#     def es_mayor_de_edad(self):
#         return self.edad >= 18

###############################################################################
#                                   PUNTO 7                                   #
###############################################################################

# class Cuenta:
#     def init(self, titular, cantidad=0):
#         self.__titular = titular
#         self.__cantidad = cantidad

#     def get_titular(self):
#         return self.__titular

#     def set_titular(self, titular):
#         self.__titular = titular

#     def get_cantidad(self):
#         return self.__cantidad

#     def ingresar(self, cantidad):
#         if cantidad > 0:
#             self.__cantidad += cantidad

#     def retirar(self, cantidad):
#         if cantidad > 0:
#             self.__cantidad -= cantidad

#     def mostrar(self):
#         print(f"Titular: {self.__titular}")
#         print(f"Cantidad: {self.__cantidad}")

###############################################################################
#                                   PUNTO 8                                   #
###############################################################################

# class CuentaJoven(Cuenta):
#     def __init__(self, titular, cantidad=0, bonificacion=0) -> None:
#         super().__init__(titular, cantidad)
#         self.__bonificacion=bonificacion

#     def get_bonificacion(self):
#         return self.__bonificacion

#     def set_bonificacion(self, bonificacion):
#         self.__bonificacion = bonificacion

#     def es_titular_valido(self):
#         return self.get_titular().edad >= 18 and self.get_titular().edad < 25

#     def retirar(self, cantidad):
#         if self.es_titular_valido():
#             super().retirar(cantidad)

#     def mostrar(self):
#         print("Cuenta Joven")
#         print("Titular:", self.get_titular().nombre)
#         print("Cantidad:", self.get_cantidad())
#         print("Bonificación:", self.__bonificacion)
