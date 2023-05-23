'''
La sentencia "continue" se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las sentencias dentro del bucle.

Se puede usar tanto con bucles while y for.

Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:

1.- un bucle for;
2.- el concepto de ejecución condicional (if-elif-else).
3.- la sentencia continue.

Tu programa debe:

1.- pedir al usuario que ingrese una palabra.
2.- utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas.
3.- utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
4.- imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada
'''

user_word = input("Ingrese una palabra: ")

user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter)
