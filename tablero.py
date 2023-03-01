import order
from colorama import init, Fore, Back, Style
##### VENTANA DEL PROGRAMA #####

imagenes = {}
gs= order.Order()

##### BOTONESINICIO #####


##### FUNCIONES #####

moves = []

win = False
first_move = []
mato = False
turno =True

# metodo ara verificar movimientos validos
def sel_piece(row, col):
    global first_move, moves, mato
    muertox =0
    muertoy =0
    first_move = [row, col]

    if gs.piece[row][col] == "fb":
        if row > 0: # para verificar el borde
            if col < 7:
                if gs.piece[row-1][col+1] == "fn" or gs.piece[row-1][col+1] == "rn": # Para saber si puede matar
                    if row-2 >= 0 and col+2 < 8:
                        if gs.piece[row-2][col+2] == "--":
                            moves.append([row-2, col+2, 1])
                            muertox=row-1
                            muertoy=col+1
                if gs.piece[row-1][col+1] == "--":
                    moves.append([row-1, col+1, 0])
            if col > 0:
                if gs.piece[row-1][col-1] == "fn"or gs.piece[row-1][col-1] == "rn":
                    if row-2 >= 0 and col-2 >= 0:
                        if gs.piece[row-2][col-2] == "--":
                            moves.append([row-2, col-2, 1])
                            muertox=row-1
                            muertoy=col-1
                if gs.piece[row-1][col-1] == "--":
                    moves.append([row-1, col-1, 0])
        print("Estos son los movimientos posibles de su ficha:")
        print("  Fila   Columna")
        for move in moves:
            print("*(",move[0],"      ",move[1],")")
    elif gs.piece[row][col] == "fn":
        if row < 7:
            if col < 7:
                if gs.piece[row+1][col+1] == "fb" or gs.piece[row+1][col+1] == "rb":
                    if row+2 < 8 and col+2 < 8:
                        if gs.piece[row+2][col+2] == "--":
                            moves.append([row+2, col+2, 1])
                            muertox=row+1
                            muertoy=col+1
                if gs.piece[row+1][col+1] == "--":
                    moves.append([row+1, col+1, 0])
            if col > 0:
                if gs.piece[row+1][col-1] == "fb" or gs.piece[row+1][col-1] == "rb":
                    if row+2 < 8 and col-2 >= 0:
                        if gs.piece[row+2][col-2] == "--":
                            moves.append([row+2, col-2, 1])
                            muertox=row+1
                            muertoy=col-1
                if gs.piece[row+1][col-1] == "--":
                    moves.append([row+1, col-1, 0])
        print("Estos son los movimientos posibles de su ficha:")
        print("  Fila   Columna")
        for move in moves:
            print("*(",move[0],"      ",move[1],")")
    elif gs.piece[row][col] == "rb":
        if row > 0:
            if col < 7:
                if gs.piece[row-1][col+1] == "fn" or gs.piece[row-1][col+1] == "rn":
                    if row-2 >= 0 and col+2 < 8:
                        if gs.piece[row-2][col+2] == "--":
                            moves.append([row-2, col+2, 1])
                            muertox=row-1
                            muertoy=col+1
                if gs.piece[row-1][col+1] == "--":
                    moves.append([row-1, col+1, 0])
            if col > 0:
                if gs.piece[row-1][col-1] == "fn"or gs.piece[row-1][col-1] == "rn":
                    if row-2 >= 0 and col-2 >= 0:
                        if gs.piece[row-2][col-2] == "--":
                            moves.append([row-2, col-2, 1])
                            muertox=row-1
                            muertoy=col-1
                if gs.piece[row-1][col-1] == "--":
                    moves.append([row-1, col-1, 0])
        if row < 7:
            if col < 7:
                if gs.piece[row+1][col+1] == "fn" or gs.piece[row+1][col+1] == "rn":
                    if row+2 < 8 and col+2 < 8:
                        if gs.piece[row+2][col+2] == "--":
                            moves.append([row+2, col+2, 1])
                            muertox=row+1
                            muertoy=col+1
                if gs.piece[row+1][col+1] == "--":
                    moves.append([row+1, col+1, 0])
            if col > 0:
                if gs.piece[row+1][col-1] == "fn" or gs.piece[row+1][col-1] == "rn":
                    if row+2 < 8 and col-2 >= 0:
                        if gs.piece[row+2][col-2] == "--":
                            moves.append([row+2, col-2, 1])
                            muertox=row+1
                            muertoy=col-1
                if gs.piece[row+1][col-1] == "--":
                    moves.append([row+1, col-1, 0])
        print("Estos son los movimientos posibles de su ficha:")
        print("  Fila   Columna")
        for move in moves:
            print("*(",move[0],"      ",move[1],")")
    elif gs.piece[row][col] == "rn":
        if row > 0:
            if col < 7:
                if gs.piece[row-1][col+1] == "fb" or gs.piece[row-1][col+1] == "rb":
                    if row-2 >= 0 and col+2 < 8:
                        if gs.piece[row-2][col+2] == "--":
                            moves.append([row-2, col+2, 1])
                            muertox=row-1
                            muertoy=col+1
                            #ARREGLANDO QUE NO SE SALGA
                if gs.piece[row-1][col+1] == "--":
                    moves.append([row-1, col+1, 0])
            if col > 0:
                if gs.piece[row-1][col-1] == "fb" or gs.piece[row-1][col-1] == "rb":
                    if row-2 >= 0 and col-2 >= 0:
                        if gs.piece[row-2][col-2] == "--":
                            moves.append([row-2, col-2, 1])
                            muertox=row-1
                            muertoy=col-1
                if gs.piece[row-1][col-1] == "--":
                    moves.append([row-1, col-1, 0])
        if row < 7:
            if col < 7:
                if gs.piece[row+1][col+1] == "fb" or gs.piece[row+1][col+1] == "rb":
                    if row+2 < 8 and col+2 < 8:    
                        if gs.piece[row+2][col+2] == "--":
                            moves.append([row+2, col+2, 1])
                            muertox=row+1
                            muertoy=col+1
                if gs.piece[row+1][col+1] == "--":
                    moves.append([row+1, col+1, 0])
            if col > 0:
                if gs.piece[row+1][col-1] == "fb" or gs.piece[row+1][col-1] == "rb":
                    if row+2 < 8 and col-2 >= 0:
                        if gs.piece[row+2][col-2] == "--":
                            moves.append([row+2, col-2, 1])
                            muertox=row+1
                            muertoy=col-1
                if gs.piece[row+1][col-1] == "--":
                    moves.append([row+1, col-1, 0])
        print("Estos son los movimientos posibles de su ficha:")
        
        print("  Fila   Columna")
        for move in moves:
            
            print("*(",move[0],"      ",move[1],")")
    else:
        print("No hay ficha en ese campo")
        viewTable()


    x1 = input("Indique la fila del campoal cual desea mover su ficha")
    if(x1!=""):
        y1 = input("Indique la fila del campoal cual desea mover su ficha")
        if(y1!=""):
            x1 = int(x1)
            y1 = int(y1)
            move_piece(first_move[0], first_move[1], x1, y1, muertox, muertoy)
    else:
        sel_piece(row, col)
    moves.clear()
    mato = False
    muertoy, muertox = 0,0


def move_piece(row, col, row2, col2, muertox, muertoy):
    global moves, turno
    #print("oreigen:",row, col," destino: ", row2, col2)

    if[row2, col2, 0] in moves:
        gs.piece[row2][col2] = gs.piece[row][col]
        gs.piece[row][col] = "--"
        turno = not turno
    elif[row2, col2, 1] in moves:
        gs.piece[row2][col2] = gs.piece[row][col]
        gs.piece[row][col] = "--"
        gs.piece[muertox][muertoy] = "--"
        turno = not turno
    else:
        if row==row2 and col==col2:
            viewTable()
        else:
            print("Movimiento inválido")
def reinas():
    #para convertir en reina azul
    if gs.piece[0][1] == "fb":
        gs.piece[0][1] = "rb"
    if gs.piece[0][3] == "fb":
        gs.piece[0][3] = "rb"
    if gs.piece[0][5] == "fb":
        gs.piece[0][5] = "rb"
    if gs.piece[0][7] == "fb":
        gs.piece[0][7] = "rb"

    #para convertir en reina roja

    if gs.piece[7][0] == "fb":
        gs.piece[7][0] = "rb"
    if gs.piece[7][2] == "fb":
        gs.piece[7][2] = "rb"
    if gs.piece[7][4] == "fb":
        gs.piece[7][4] = "rb"
    if gs.piece[7][6] == "fb":
        gs.piece[7][6] = "rb"

#MOSTRAR TABLERO
def instructions():
    print("**************************************")
    print(" BIENVENIDO AL JUEGO DE DAMAS INGLESAS")
    print("**************************************")
    print("Para tener en cuenta las fichas de los ")
    print("jugadores están identificadas así: 'fn'")
    print("significa ficha negra, 'fb' siganifica ")
    print("ficha blanca, 'rn' significa reina ")
    print("negra, 'rb' significa reina blanca")
    print("**************************************")
    print("")
    print("************************************************")
    print("                    TABLERO")
    print("************************************************")
    print("")


def viewTable():
    global turno, win
    filas=[' ','F','I','L','A','S',' ',' ']
    print("            C O L U M N A S")
    print(" 0   1    2    3    4    5    6    7")
    print("__________________________________________")
    reinas()
    board_size = 8
    for row in range(board_size):
        for col in range(board_size):
            if gs.piece[row][col]=="--":
                print(Fore.WHITE + gs.piece[row][col], "  ", end="")
            elif gs.piece[row][col]=="fb" or gs.piece[row][col]=="rb":
                print(Fore.BLUE + gs.piece[row][col],"  ", end="")
            elif gs.piece[row][col]=="fn" or gs.piece[row][col]=="rn":
                print(Fore.RED + gs.piece[row][col],"  ", end="")
        print( " ", Fore.WHITE+"{}".format(row)," ",filas[row])
    if turno:
        print("Juega Azul")
        x = input("Indique la fila de la ficha que desea mover")
        if(x!=""):
            y = input("Indique la columna de la ficha que desea mover")
            if (y!=""):
                x = int(x)
                y = int(y)
                if x>8:
                    print("no existe fila  ", x)
                    viewTable()
                elif y > 8:
                    print("no existe columna  ", y)
                    viewTable()
                else:
                    if(gs.piece[x][y]=="fn" or gs.piece[x][y]=="rn"):
                        print("No es turno de Rojo")
                        viewTable()
                    else:
                        sel_piece(x,y)
            else:
                print("Por favor digite un valor ")
                viewTable()
        else:
            print("Por favor ingrese un valor")
            viewTable()
    else:
        print("Juega Rojo")
        x = input("Indique la fila de la ficha que desea mover")
        if(x!=""):
            y = input("Indique la columna de la ficha que desea mover")
            if (y!=""):
                x = int(x)
                y = int(y)
                if x>8:
                    print("no existe fila  ", x)
                    viewTable()
                elif y > 8:
                    print("no existe columna  ", y)
                    viewTable()
                else:
                    if(gs.piece[x][y]=="fb" or gs.piece[x][y]=="rb"):
                        print("No es turno de Azul")
                        viewTable()
                    else:
                        sel_piece(x,y)
            else:
                print("Por favor digite un valor ")
                viewTable()
        else:
            print("Por favor ingrese un valor")
            viewTable()
    
    contW = 0
    contB = 0
    for row in gs.piece:
        for elemento in row:
            if elemento == "fb":
                contW+=1
            elif elemento == "fn" or elemento =="rn":
                contB+=1
    if contB == 0:
        print("Azul ha ganado")
        win= True
    elif contW == 0:
        print("Rojo ha ganado")
        win= True

##### BUCLE PRINCIPAL PROGRAMA #####

instructions()
while not win:
    viewTable()

