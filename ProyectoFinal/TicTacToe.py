'''
Escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar 
el juego. Aquí están nuestras reglas:

1.- la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
2.- el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
3.- el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
4.- todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
5.- el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor 
entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
6.- el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: 
el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
7.- la maquina responde con su movimiento y se verifica el estado del juego;
8.- no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.

El ejemplo del programa es el siguiente:

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Ingresa tu movimiento: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
¡Has Ganado!


Implementa las siguientes características:

1.- el tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos 
(la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:
board[row][column]

2.- cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número del cuadro 
(dicho cuadro se considera como libre)

3.- la apariencia de tablero debe de ser igual a la presentada en el ejemplo.

Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada randrange(). 
El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

from random import randrange
 
for i in range(10):
    print(randrange(8))

Nota: la instrucción from-import provee acceso a la función randrange definida en un módulo externo de Python denominado random.
'''

from random import randrange # Función para números aleatorios

board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Definición del tablero de juego

# La función acepta un parámetro el cual contiene el estado actual del tablero y lo muestra en la consola.
def display_board(board):
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       |       |       |")
        print("+-------+-------+-------+")
    make_list_of_free_fields(board)


# La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
def enter_move(board):
    while True:
        try:
            move = int(input("Ingresa tu movimiento: ")) - 1
            #move -= 1
            if move not in range(9) or free_fields[move] == 0:
                print("Debes ingresar un número válido (del 1 al 9) y que no haya sido jugado")
            else:
                board[free_fields[move][0]][free_fields[move][1]] = "O"
                break
        except:
            print("ERROR --- El valor ingresado no es de tipo válido.")
    display_board(board)
    victory_for(board, "O")


# La función examina el tablero y construye una lista de todos los cuadros vacíos. 
# La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
# si esa posición ya fue jugada, guarda un "0"
def make_list_of_free_fields(board):
    global free_fields
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ("X", "O"):
                free_fields.append((row, col))
            else:
                free_fields.append(0)


# La función analiza el estatus del tablero para verificar si el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
def victory_for(board, sign):
    global victory
    if free_fields.count(0) >= 5:    # Mientras haya menos de 5 jugadas entre ambos jugadores, no puede haber aún una victoria
        # Se evaluan las filas
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] == sign: 
                victory = True
        # Se evaluan las columnas
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == sign:
                victory = True
        # Se evaluan las diagonales
        if board[0][0] == board[1][1] == board[2][2] == sign or board[0][2] == board[1][1] == board[2][0] == sign:
            victory = True
            
        if not victory and free_fields.count(0) == 9: print("¡Ha sido un empate!")
        if victory:
            if sign == "X": 
                print("¡La máquina ha ganado!")
            else:
                print("¡Has Ganado!")
        


# La función dibuja el movimiento de la máquina y actualiza el tablero.
def draw_move(board):
    if board[1][1] == 5:
        board[1][1] = "X"
    else:
        move = 5
        while free_fields[move] == 0:
            move = randrange(9) - 1
        board[free_fields[move][0]][free_fields[move][1]] = "X"        
    display_board(board)
    victory_for(board, "X")


victory = False

while not victory:
    if not victory: draw_move(board)
    if not victory: enter_move(board)
