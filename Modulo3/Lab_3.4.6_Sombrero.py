'''
Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.

Tu tarea es:

1.- escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero 
ingresado por el usuario (Paso 1)
2.- escribir una línea de código que elimine el último elemento de la lista (Paso 2)
3.- escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
'''

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
new = int(input("Inserta el nuevo número: "))
hat_list[2] = new

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[-1]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print(len(hat_list))

print(hat_list)
