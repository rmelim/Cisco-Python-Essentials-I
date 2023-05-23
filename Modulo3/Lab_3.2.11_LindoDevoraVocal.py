'''
Tu tarea aquí es aún más especial que antes: ¡Debes rediseñar el devorador de vocales (feo) del laboratorio anterior y crear un mejor 
devorador de vocales (lindo) mejorado! Escribe un programa que use:

1.- un bucle for.
2.- el concepto de ejecución condicional (if-elif-else).
3.- la instrucción continue.

Tu programa debe:

1.- pedir al usuario que ingrese una palabra.
2.- utilizar user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas.
3.- emplea la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A , E , I , O , U de la palabra ingresada.
4.- asigna las letras no consumidas a la variable word_without_vowels e imprime la variable en la pantalla.

Hemos creado word_without_vowels y le hemos asignado una cadena vacía. 
Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en una cadena más larga durante los siguientes 
giros de bucle, y asignarlo a la variable word_without_vowels.
'''

word_without_vowels = ""

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
        word_without_vowels += letter
    
print(word_without_vowels)
