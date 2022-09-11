from os import system

print("""
Bienvenidos a la segunda lección de Python.
Ahora procederemos a trabajar con los operadores de comparación y datos booleanos.
""")
print()
print("""
Ya habíamos hablado antes de la declaración de variables, los tipos de datos y las operaciones aritméticas.
""")
print(input("Ahora vamos a conocer los operadores lógicos. (Press Enter)"))

# Los operadores de comparación son los que se utilizan para comparar dos valores
# Es decir podemos comparar entre dos variables distintas la información contenida.

print("""
Los operadores lógicos son los siguientes:
# Mayor que     ---->  ">"
# Menor que     ---->  "<"
# Igual a       ---->  "=="
# Mayor o igual ---->  ">="
# Menor o igual ---->  "<="
# No igual      ---->  "!="
""")

# Las operaciones de comparación con dichos valores nos generarán un valor de tipo booleano

print(input("Ejemplos de operaciones de comparación"))

system('cls')

print("""
# Declaramos variables de tipo "int" o de tipo "float"

variable1 = 500
variable2 = 1000
variable3 = 1000
variable4 = 200

# Una vez declaradas las variables procedemos a realizar una operación logica. El resultado de una comparación
# debe almacenarse en otra variable cuyo tipo de dato será booleano.

comparacion1 = variable1 > variable3
comparacion2 = variable3 == variable2
comparacion3 = variable1 <= variable4
""")

variable1 = 500
variable2 = 1000
variable3 = 1000
variable4 = 200

comparacion1 = variable1 > variable3
comparacion2 = variable3 == variable2
comparacion3 = variable1 <= variable4

# En la clase anterior aprendiste los tipos de datos que puede manejar una variable, pero si eres perspicaz
# te darás cuenta que no utilizamos el tipo de dato booleano para realizar operaciones aritméticas y esto es
# debido a que los datos booleanos solo tienen dos posibles resultados, True o False, los cuales no pueden
# ser utilizados en las operaciones aritméticas, no podemos sumar True más True o cualquier combinación.

print(input("Vamos a verificar el tipo de dato de las variables en las cuales guardamos el resultado (Press Enter)"))
print(type(comparacion1))
print(type(comparacion2))
print(type(comparacion3))

print(input("Ahora imprimamos el valor de las variables"))
print("comparación1 = ", comparacion1)
print("comparación2 = ", comparacion2)
print("comparación3 = ", comparacion3)
