print("""
# 1. Python es un lenguaje de programación interpretado
# 2. Es multi-paradigma [Programación Web, Videojuegos, Ciencia de Datos]
# 3. Es multi-plataforma [Funciona en S.O. Windows, Linux y Unix(Mac)]

# Iniciando con la sintaxis básica de Python

# Declaración de variables y tipos de datos
""")

# VARIABLES: Espacio de memoria en el que se almacena información, que puede ser utilizada posteriormente.

variableCharacter = 'Aprendiendo Python'  # ---------> Variable de Tipo String ~ Cadena de Caracteres
variableInteger = 512  # ---------> Variable de Tipo Integer ~ Números Enteros
variableFloat = 3.1416  # ---------> Variable de Tipo Float ~ Números Decimales
variableBoolean = True  # ---------> Variable de Tipo Boolean ~ Valores de Falso y Verdadero

print(""""
VARIABLES: Espacio de memoria en el que se almacena información, que puede ser utilizada posteriormente.

variableCharacter = 'Aprendiendo Python'  # ---------> Variable de Tipo String ~ Cadena de Caracteres
variableInteger = 512                     # ---------> Variable de Tipo Integer ~ Números Enteros
variableFloat = 3.1416                    # ---------> Variable de Tipo Float ~ Números Decimales
variableBoolean = True                    # ---------> Variable de Tipo Boolean ~ Valores de Falso y Verdadero
""")

# Comprobación de Tipo de Dato ~ En Python podemos usar la función 'type' para conocer el tipo de dato de una variable
print(type(variableCharacter))
print(type(variableInteger))
print(type(variableFloat))
print(type(variableBoolean))

print(input("Reasignación de valores con operaciones aritméticas (Press Enter)"))

# Reasignación de valores a las variables con operaciones aritméticas
entero1 = 700
entero2 = 12
sumaEntero = entero1 + entero2  # Suma el valor de la variable 1 más la variable 2
restaEntero = entero1 - entero2  # Resta el valor de la variable 1 menos la variable 2
divisionEntero = entero1 / entero2  # Divide el valor de la variable 1 entre a la variable 2
multiplicacionEntero = entero1 * entero2  # Multiplica el valor de la variable 1 por la variable 2
potenciaEntero = entero1 ** entero2  # Devuelve el producto de la potencia
restoEntero = entero1 % entero2  # Divide la variable 1 entre la variable 2 y devuelve el resto
divisionExactaEntero = entero1 // entero2  # Divide la variable 1 entre la variable 2 sin decimales

print("""

# Reasignación de valores a las variables con operaciones aritméticas

entero1 = 700
entero2 = 12
sumaEntero = entero1 + entero2                  # Suma el valor de la variable 1 más la variable 2
restaEntero = entero1 - entero2                 # Resta el valor de la variable 1 menos la variable 2
divisionEntero = entero1 / entero2              # Divide el valor de la variable 1 entre a la variable 2
multiplicacionEntero = entero1 * entero2        # Multiplica el valor de la variable 1 por la variable 2
potenciaEntero = entero1 ** entero2             # Devuelve el producto de la potencia
restoEntero = entero1 % entero2                 # Divide la variable 1 entre la variable 2 y devuelve el resto
divisionExactaEntero = entero1 // entero2       # Divide la variable 1 entre la variable 2 sin decimales

""")

print(input("Realizar Operaciones (Press Enter)"))

print("Resultados de la operaciones anteriores")
print("sumaEntero = entero1 + entero2: --> ", sumaEntero)
print("restaEntero = entero1 - entero2: --> ", restoEntero)
print("divisionEntero = entero1 / entero2: --> ", divisionEntero)
print("multiplicacionEntero = entero1 * entero2: --> ", multiplicacionEntero)
print("potenciaEntero = entero1 ** entero2: --> ", potenciaEntero)
print("restoEntero = entero1 % entero2: --> ", restoEntero)
print("divisionExactaEntero = entero1 // entero2: --> ", divisionExactaEntero)

# Verifiquemos ahora el tipo de dato de las variables
print(input("Verificar tipo de dato (Press Enter)"))
print("Los tipos de dato se asignan automáticamente en Python, no es necesario declararlos.")
print(type(sumaEntero))
print(type(restaEntero))
print(type(divisionEntero))
print(type(multiplicacionEntero))
print(type(potenciaEntero))
print(type(restoEntero))
print(type(divisionExactaEntero))

# Concatenación de Strings
print(input("También se pueden concatenar cadenas de caracteres (Press Enter)"))
cadena1 = "Estoy aprendiendo "
cadena2 = "a usar el lenguaje "
cadena3 = "de programación ¡Python!."

print("""

cadena1 = "Estoy aprendiendo "
cadena2 = "a usar el lenguaje "
cadena3 = "de programación ¡Python!."

concantenacion = cadena1 + cadena2 + cadena3

""")

print("Este código va a unir la información de nuestras tres variables para guardarla en una.")
print(input("Realizar la operación (Press Enter)"))

concantenacion = cadena1 + cadena2 + cadena3
print(concantenacion)

print("""
# Para finalizar es importante mencionar que las variables de tipo Boolean no pueden ser utilizadas en OP. Aritméticas
""")

print(input("Por ahora es todo, ¡Gracias por ver! (Press Enter to finish)"))
