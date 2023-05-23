'''
Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada secret_number. Quiere que todos los que ejecutan su programa 
jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos. ¡Quiénes no adivinen el número quedarán atrapados en un 
bucle sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

1.- pedirá al usuario que ingrese un número entero;
2.- utilizará un bucle while;
3.- comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. 
4.- Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver 
el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. 
5.- Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse 
en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."

INFO EXTRA  
Observa la función print(). La forma en que lo hemos utilizado aquí se llama impresión multilínea. 
Puedes utilizar comillas triples para imprimir cadenas en varias líneas para facilitar la lectura del texto o crear un diseño especial basado en texto. 
'''

secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

number = 0

while number != secret_number:
    number = int(input("Ingrese un número entero: "))
    if number != secret_number:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")

print("¡Bien hecho, muggle! Eres libre ahora.")
