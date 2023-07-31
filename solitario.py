# librerias
import random
import os

# variables
negras = ['♠', '♣'] #cartas negras
rojas = ['♥', '♦'] #cartas rojas

baraja = [] #almacena las cartas pero no se ven en el menu
carta = ["1♥", "1♦", "1♠", "1♣", "2♥", "2♦", "2♠", "2♣", "3♥", "3♦", "3♠", "3♣", "4♥", "4♦", "4♠", "4♣", "5♥", "5♦",
        "5♠", "5♣", "6♥", "6♦", "6♠", "6♣", "7♥", "7♦", "7♠", "7♣", "8♥", "8♦", "8♠", "8♣", "9♥", "9♦", "9♠", "9♣",
        "10♥", "10♦", "10♠", "10♣", "J♥", "J♦", "J♠", "J♣", "Q♥", "Q♦", "Q♠", "Q♣", "K♥", "K♦", "K♠", "K♣"]
pila1 = [] #mano1 o mazo1
pila2 = [] #mano2 o mazo2
pila3 = [] #mano3 o mazo3
pila4 = [] #mano4 o mazo4
pila5 = [] #mano5 o mazo5
pila6 = [] #mano6 o mazo6
pila7 = [] #mano7 o mazo7
pila8 = []#trebol
pila9 = []#diamante
pila10 = []#corazon
pila11 = []#pica
pila12 = [] #cartas que tomamos de la baraja

ganadas = 0    #estadisticas ganadas
perdidas = 0   #estadisticas perdidas

# metodos

#crear baraja
def crearBaraja():
    for i in range(52): #En un rango de 52
            baraja.append(carta[i]) #agrega las cartas a la baraja y las quita de la lista carta
    random.shuffle(baraja) #baraja las cartas de forma aletoria y las agrega a la baraja

#repartir las cartas en cada mano
def repartir():
    for i in range(1):               #mano1
        pila1.append(baraja.pop())   #agrega una carta a la mano1 y la quita de la baraja
    for i in range(2):               #mano2
        pila2.append(baraja.pop())
    for i in range(3):               #mano3
        pila3.append(baraja.pop())
    for i in range(4):               #mano4
        pila4.append(baraja.pop())
    for i in range(5):               #mano5
        pila5.append(baraja.pop())
    for i in range(6):               #mano6
        pila6.append(baraja.pop())
    for i in range(7):               #mano7
        pila7.append(baraja.pop())

#valida orden decendente de las cartas y signo para que intercale entre rojo y negro una a una
def validarMovimiento(carta_origen, carta_destino=False): # = False signinifica que si no le mando el argumento (carta_destino) lo pone falso

    if carta_destino == False: 
        return True 

    origenP = carta_origen[-1] #palo de la carta origen, el -1 es para que agarre el ultimo caracter de la cadena
    origenN = carta_origen[0] #numero de la carta origen, el 0 es para que agarre el primer caracter de la cadena

    destinoP = carta_destino[-1] #palo de la carta destino, el -1 es para que agarre el ultimo caracter de la cadena
    destinoN = carta_destino[0] #numero de la carta destino, el 0 es para que agarre el primer caracter de la cadena

    if origenN == 'K': #si la carta origen es K que sea igual a 13
        origenN = 13
    if origenN == 'Q': #si la carta origen es Q que sea igual a 12
        origenN = 12
    if origenN == 'J': #si la carta origen es J que sea igual a 11
        origenN = 11
    if destinoN == 'K': #si la carta destino es K que sea igual a 13
        destinoN = 13
    if destinoN == 'Q': #si la carta destino es Q que sea igual a 12
        destinoN = 12
    if destinoN == 'J': #si la carta destino es J que sea igual a 11
        destinoN = 11

    origenN = int(origenN) #convierte el numero de la carta origen a entero
    destinoN = int(destinoN) #convierte el numero de la carta destino a entero

    if origenP in rojas: #si el palo de la carta origen es rojo
        if destinoP in negras: #si el palo de la carta destino es negra
            
            if destinoN == origenN + 1: #esta en orden decendente
                return True #retorna verdadero osea que si se cumple la accion
            else: #si no esta en orden decendente
                return False #retorna falso osea que no se cumple la accion
#caso contrario al de arriba para los colores
    if origenP in negras: 
        if destinoP in rojas:    
            if destinoN == origenN + 1:
                return True
            else:
                return False

    else: # si son del mismo color
        return False #no se cumple la accion

#valida orden decendente de las cartas y signo para que intercale entre rojo y negro al mover varias
def validarMovimientoCartas(cartas, destino=False): 
    if destino == False:
        return True

    if validarMovimiento(cartas[-1], cartas[-2]): #si la ultima carta de la lista de cartas es valida con la penultima, utilizando el "validar movimiento"
        return True
    return False

#mover cartas de las pilas
def moverPilas():
    print("Mover de pila a pila")
    try:#intente
        pilaOrigen = int(input("Pila origen: "))#pregunta la pila de origen
        pilaDestino = int(input("Pila destino: "))#pregunta la pila de destino
    except ValueError: #si no es un valor valido
        print("Error, esa no es una opcion") #imprime error
        print("desea volver a intentar? (s/n)") #pregunta si desea continuar
        if input() == "s":
            return moverPilas() #vuelve a preguntar las pilas de origen y destino
        else:
            return mostrarMenu(intentos) #si no desea continuar vuelve al menu

    if pilaOrigen == 0:#baraja
        if len(pila12) == 0: #si la pila12(la que muestras las cartas tomadas de la baraja) esta vacia
            print("No hay cartas en la baraja") #imprime que no hay cartas en la baraja
            return moverPilas() #vuelve a preguntar las pilas de origen y destino
        else: #si no esta vacia
            if pilaDestino == 1: #si la pila de destino es 1
                    pila1.append(pila12.pop()) #agrega la carta a la pila1 y la quita de la pila12
            elif pilaDestino == 2:
                pila2.append(pila12.pop())
            elif pilaDestino == 3:
                pila3.append(pila12.pop())
            elif pilaDestino == 4:
                pila4.append(pila12.pop())
            elif pilaDestino == 5:
                pila5.append(pila12.pop())
            elif pilaDestino == 6:
                pila6.append(pila12.pop())
            elif pilaDestino == 7:
                pila7.append(pila12.pop())
            elif pilaDestino == 8: #si la pila de destino es 8
                if pila12[-1][-1] == "♣": #si el ultimo caracter de la ultima carta de la pila12 es ♣
                    if len (pila8) == 0: #si la pila8 esta vacia
                        if pila12[-1] == "1♣": #si la ultima carta de la pila12 es 1♣
                            pila8.append(pila12.pop()) #agrega la carta a la pila8 y la quita de la pila12
                        else: #si no es 1♣
                            print("No puedes poner una carta diferente de 1♣ de primera carta") #imprime que no puedes poner una carta diferente de 1♣ de primera carta
                    else: #si la pila8 no esta vacia
                        value0 = pila12[-1][0] #el valor de la ultima carta de la pila12 es el primer caracter de la ultima carta de la pila12
                        value1 = pila8[-1][0] #el valor de la ultima carta de la pila8 es el primer caracter de la ultima carta de la pila8
                        if value0 == 'K': 
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1: #si el valor de la ultima carta de la pila8 es igual al valor de la ultima carta de la pila12 menos 1(ascendente)
                            pila8.append(pila12.pop()) #agrega la carta a la pila8 y la quita de la pila12
                        else:
                            print("Carta no es la siguiente") #imprime que la carta no es la siguiente
                else:
                    print("no puedes poner esta carta") #imprime que no puedes poner esta carta
            elif pilaDestino == 9:
                if pila12[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila12[-1] == "1♦":
                            pila9.append(pila12.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila12[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila9.append(pila12.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila12[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila12[-1] == "1♥":
                            pila10.append(pila12.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila12[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila10.append(pila12.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila12[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila12[-1] == "1♠":
                            pila11.append(pila12.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila12[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila11.append(pila12.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
    elif pilaOrigen == 1:#mano1
        if len(pila1) == 0:
            print("No hay cartas en la baraja")
            return moverPilas()
        else:
            if pilaDestino == 2:
                if validarMovimiento(pila1[-1], pila2[-1] if len(pila2) != 0 else False): # operador ternario
                    pila2.append(pila1.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 3:
                if validarMovimiento(pila1[-1], pila3[-1] if len(pila3) != 0 else False):
                    pila3.append(pila1.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 4:
                if validarMovimiento(pila1[-1], pila4[-1] if len(pila4) != 0 else False):
                    pila4.append(pila1.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 5:
                if validarMovimiento(pila1[-1], pila5[-1] if len(pila5) != 0 else False):
                    pila5.append(pila1.pop())
            elif pilaDestino == 6:
                if validarMovimiento(pila1[-1], pila6[-1] if len(pila6) != 0 else False):
                    pila6.append(pila1.pop())
            elif pilaDestino == 7:
                if validarMovimiento(pila1[-1], pila7[-1] if len(pila7) != 0 else False):
                    pila7.append(pila1.pop())
            elif pilaDestino == 8:
                if pila1[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila1[-1] == "1♣":
                            pila8.append(pila1.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila1[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila8.append(pila1.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila1[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila1[-1] == "1♦":
                            pila9.append(pila1.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila1[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila9.append(pila1.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila1[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila1[-1] == "1♥":
                            pila10.append(pila1.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila1[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila10.append(pila1.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila1[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila1[-1] == "1♠":
                            pila11.append(pila1.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila1[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila11.append(pila1.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
    elif pilaOrigen == 2:#mano2
        if len(pila2) == 0:
            print("No hay cartas en la baraja")
            return moverPilas()
        else:
            if pilaDestino == 1:
                if validarMovimiento(pila2[-1], pila1[-1] if len(pila1) != 0 else False):
                    pila1.append(pila2.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 3:
                if validarMovimiento(pila2[-1], pila3[-1] if len(pila3) != 0 else False):
                    pila3.append(pila2.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 4:
                if validarMovimiento(pila2[-1], pila4[-1] if len(pila4) != 0 else False):
                    pila4.append(pila2.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 5:
                if validarMovimiento(pila2[-1], pila5[-1] if len(pila5) != 0 else False):
                    pila5.append(pila2.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 6:
                if validarMovimiento(pila2[-1], pila6[-1] if len(pila6) != 0 else False):
                    pila6.append(pila2.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 7:
                if validarMovimiento(pila2[-1], pila7[-1] if len(pila7) != 0 else False):
                    pila7.append(pila2.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 8:
                if pila2[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila2[-1] == "1♣":
                            pila8.append(pila2.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila2[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila8.append(pila2.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila2[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila2[-1] == "1♦":
                            pila9.append(pila2.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila2[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila9.append(pila2.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila2[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila2[-1] == "1♥":
                            pila10.append(pila2.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila2[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila10.append(pila2.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila2[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila2[-1] == "1♠":
                            pila11.append(pila2.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila2[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila11.append(pila2.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
    elif pilaOrigen == 3:#mano3
        if len(pila3) == 0:
            print("No hay cartas en la baraja")
            return moverPilas()
        else:
            if pilaDestino == 1:
                if validarMovimiento(pila3[-1], pila1[-1] if len(pila1) != 0 else False):
                    pila1.append(pila3.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 2:
                if validarMovimiento(pila3[-1], pila2[-1] if len(pila2) != 0 else False):
                    pila2.append(pila3.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 4:
                if validarMovimiento(pila3[-1], pila4[-1] if len(pila4) != 0 else False):
                    pila4.append(pila3.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 5:
                if validarMovimiento(pila3[-1], pila5[-1] if len(pila5) != 0 else False):
                    pila5.append(pila3.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 6:
                if validarMovimiento(pila3[-1], pila6[-1] if len(pila6) != 0 else False):
                    pila6.append(pila3.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 7:
                if validarMovimiento(pila3[-1], pila7[-1] if len(pila7) != 0 else False):
                    pila7.append(pila3.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 8:
                if pila3[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila3[-1] == "1♣":
                            pila8.append(pila3.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila3[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila8.append(pila3.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila3[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila3[-1] == "1♦":
                            pila9.append(pila3.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila3[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila9.append(pila3.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila3[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila3[-1] == "1♥":
                            pila10.append(pila3.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila3[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila10.append(pila3.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila3[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila3[-1] == "1♠":
                            pila11.append(pila3.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila3[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila11.append(pila3.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
    elif pilaOrigen == 4:#mano4
        if len(pila4) == 0:
            print("No hay cartas en la baraja")
            return moverPilas()
        else:
            if pilaDestino == 1:
                if validarMovimiento(pila4[-1], pila1[-1] if len(pila1) != 0 else False):
                    pila1.append(pila4.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 2:
                if validarMovimiento(pila4[-1], pila2[-1] if len(pila2) != 0 else False):
                    pila2.append(pila4.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 3:
                if validarMovimiento(pila4[-1], pila3[-1] if len(pila3) != 0 else False):
                    pila3.append(pila4.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 5:
                if validarMovimiento(pila4[-1], pila5[-1] if len(pila5) != 0 else False):
                    pila5.append(pila4.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 6:
                if validarMovimiento(pila4[-1], pila6[-1] if len(pila6) != 0 else False):
                    pila6.append(pila4.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 7:
                if validarMovimiento(pila4[-1], pila7[-1] if len(pila7) != 0 else False):
                    pila7.append(pila4.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 8:
                if pila4[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila4[-1] == "1♣":
                            pila8.append(pila4.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila4[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila8.append(pila4.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila4[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila4[-1] == "1♦":
                            pila9.append(pila4.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila4[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila9.append(pila4.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila4[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila4[-1] == "1♥":
                            pila10.append(pila4.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila4[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila10.append(pila4.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila4[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila4[-1] == "1♠":
                            pila11.append(pila4.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila4[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila11.append(pila4.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
    elif pilaOrigen == 5:#mano5
        if len(pila5) == 0:
            print("No hay cartas en la baraja")
            return moverPilas()
        else:
            if pilaDestino == 1:
                if validarMovimiento(pila5[-1], pila1[-1] if len(pila1) != 0 else False):
                    pila1.append(pila5.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 2:
                if validarMovimiento(pila5[-1], pila2[-1] if len(pila2) != 0 else False):
                    pila2.append(pila5.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 3:
                if validarMovimiento(pila5[-1], pila3[-1] if len(pila3) != 0 else False):
                    pila3.append(pila5.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 4:
                if validarMovimiento(pila5[-1], pila4[-1] if len(pila4) != 0 else False):
                    pila4.append(pila5.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 6:
                if validarMovimiento(pila5[-1], pila6[-1] if len(pila6) != 0 else False):
                    pila6.append(pila5.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 7:
                if validarMovimiento(pila5[-1], pila7[-1] if len(pila7) != 0 else False):
                    pila7.append(pila5.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 8:
                if pila5[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila5[-1] == "1♣":
                            pila8.append(pila5.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila5[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila8.append(pila5.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila5[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila5[-1] == "1♦":
                            pila9.append(pila5.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila5[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila9.append(pila5.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila5[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila5[-1] == "1♥":
                            pila10.append(pila5.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila5[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila10.append(pila5.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila5[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila5[-1] == "1♠":
                            pila11.append(pila5.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila5[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila11.append(pila5.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
    elif pilaOrigen == 6:#mano6
        if len(pila6) == 0:
            print("No hay cartas en la baraja")
            return moverPilas()
        else:
            if pilaDestino == 1:
                if validarMovimiento(pila6[-1], pila1[-1] if len(pila1) != 0 else False):
                    pila1.append(pila6.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 2:
                if validarMovimiento(pila6[-1], pila2[-1] if len(pila2) != 0 else False):
                    pila2.append(pila6.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 3:
                if validarMovimiento(pila6[-1], pila3[-1] if len(pila3) != 0 else False):
                    pila3.append(pila6.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 4:
                if validarMovimiento(pila6[-1], pila4[-1] if len(pila4) != 0 else False):
                    pila4.append(pila6.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 5:
                if validarMovimiento(pila6[-1], pila5[-1] if len(pila5) != 0 else False):
                    pila5.append(pila6.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 7:
                if validarMovimiento(pila6[-1], pila7[-1] if len(pila7) != 0 else False):
                    pila7.append(pila6.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 8:
                if pila6[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila6[-1] == "1♣":
                            pila8.append(pila6.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila6[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila8.append(pila6.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila6[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila6[-1] == "1♦":
                            pila9.append(pila6.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila6[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila9.append(pila6.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila6[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila6[-1] == "1♥":
                            pila10.append(pila6.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila6[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila10.append(pila6.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila6[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila6[-1] == "1♠":
                            pila11.append(pila6.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila6[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila11.append(pila6.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
    elif pilaOrigen == 7:#mano7
        if len(pila7) == 0:
            print("No hay cartas en la baraja")
            return moverPilas()
        else:
            if pilaDestino == 1:
                if validarMovimiento(pila7[-1], pila1[-1] if len(pila1) != 0 else False):
                    pila1.append(pila7.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 2:
                if validarMovimiento(pila7[-1], pila2[-1] if len(pila2) != 0 else False):
                    pila2.append(pila7.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 3:
                if validarMovimiento(pila7[-1], pila3[-1]  if len(pila3) != 0 else False):
                    pila3.append(pila7.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 4:
                if validarMovimiento(pila7[-1], pila4[-1] if len(pila4) != 0 else False):
                    pila4.append(pila7.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 5:
                if validarMovimiento(pila7[-1], pila5[-1] if len(pila5) != 0 else False):
                    pila5.append(pila7.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 6:
                if validarMovimiento(pila7[-1], pila6[-1] if len(pila6) != 0 else False):
                    pila6.append(pila7.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 8:
                if pila7[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila7[-1] == "1♣":
                            pila8.append(pila7.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila7[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila8.append(pila7.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila7[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila7[-1] == "1♦":
                            pila9.append(pila7.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila7[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila9.append(pila7.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila7[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila7[-1] == "1♥":
                            pila10.append(pila7.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila7[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila10.append(pila7.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila7[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila7[-1] == "1♠":
                            pila11.append(pila7.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila7[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila11.append(pila7.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
    elif pilaOrigen == 8:#♣
        if len(pila8) == 0:
            print("No hay cartas en la baraja")
            return moverPilas()
        else:
            if pilaDestino == 1:
                if validarMovimiento(pila8[-1], pila1[-1]):
                    pila1.append(pila8.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 2:
                if validarMovimiento(pila8[-1], pila2[-1]):
                    pila2.append(pila8.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 3:
                if validarMovimiento(pila8[-1], pila3[-1]):
                    pila3.append(pila8.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 4:
                if validarMovimiento(pila8[-1], pila4[-1]):
                    pila4.append(pila8.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 5:
                if validarMovimiento(pila8[-1], pila5[-1]):
                    pila5.append(pila8.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 6:
                if validarMovimiento(pila8[-1], pila6[-1]):
                    pila6.append(pila8.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 7:
                if validarMovimiento(pila8[-1], pila7[-1]):
                    pila7.append(pila8.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 9:
                if pila8[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila8[-1] == "1♦":
                            pila9.append(pila8.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila8[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila9.append(pila8.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila8[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila8[-1] == "1♥":
                            pila10.append(pila8.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila8[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila10.append(pila8.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila8[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila8[-1] == "1♠":
                            pila11.append(pila8.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila8[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila11.append(pila8.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
    elif pilaOrigen == 9:#♦
        if len(pila9) == 0:
            print("No hay cartas en la baraja")
            return moverPilas()
        else:
            if pilaDestino == 1:
                if validarMovimiento(pila9[-1], pila1[-1]):
                    pila1.append(pila9.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 2:
                if validarMovimiento(pila9[-1], pila2[-1]):
                    pila2.append(pila9.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 3:
                if validarMovimiento(pila9[-1], pila3[-1]):
                    pila3.append(pila9.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 4:
                if validarMovimiento(pila9[-1], pila4[-1]):
                    pila4.append(pila9.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 5:
                if validarMovimiento(pila9[-1], pila5[-1]):
                    pila5.append(pila9.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 6:
                if validarMovimiento(pila9[-1], pila6[-1]):
                    pila6.append(pila9.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 7:
                if validarMovimiento(pila9[-1], pila7[-1]):
                    pila7.append(pila9.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 8:
                if pila9[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila9[-1] == "1♣":
                            pila8.append(pila9.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila9[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila8.append(pila9.pop())
                        else:
                            print("Carta no es la siguiente")
            elif pilaDestino == 10:
                if pila9[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila9[-1] == "1♥":
                            pila10.append(pila9.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila9[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila10.append(pila9.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila9[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila9[-1] == "1♠":
                            pila11.append(pila9.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila9[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila11.append(pila9.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
    elif pilaOrigen == 10:#♥
        if len(pila10) == 0:
            print("No hay cartas en la baraja")
            return moverPilas()
        else:
            if pilaDestino == 1:
                if validarMovimiento(pila10[-1], pila1[-1]):
                    pila1.append(pila10.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 2:
                if validarMovimiento(pila10[-1], pila2[-1]):
                    pila2.append(pila10.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 3:
                if validarMovimiento(pila10[-1], pila3[-1]):
                    pila3.append(pila10.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 4:
                if validarMovimiento(pila10[-1], pila4[-1]):
                    pila4.append(pila10.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 5:
                if validarMovimiento(pila10[-1], pila5[-1]):
                    pila5.append(pila10.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 6:
                if validarMovimiento(pila10[-1], pila6[-1]):
                    pila6.append(pila10.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 7:
                if validarMovimiento(pila10[-1], pila7[-1]):
                    pila7.append(pila10.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 8:
                if pila10[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila10[-1] == "1♣":
                            pila8.append(pila10.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila10[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila8.append(pila10.pop())
                        else:
                            print("Carta no es la siguiente")
            elif pilaDestino == 9:
                if pila10[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila10[-1] == "1♦":
                            pila9.append(pila10.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila10[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila9.append(pila10.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila10[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila10[-1] == "1♠":
                            pila11.append(pila10.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila10[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila11.append(pila10.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
    elif pilaOrigen == 11:#♠
        if len(pila11) == 0:
            print("No hay cartas en la baraja")
            return moverPilas()
        else:
            if pilaDestino == 1:
                if validarMovimiento(pila11[-1], pila1[-1]):
                    pila1.append(pila11.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 2:
                if validarMovimiento(pila11[-1], pila2[-1]):
                    pila2.append(pila11.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 3:
                if validarMovimiento(pila11[-1], pila3[-1]):
                    pila3.append(pila11.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 4:
                if validarMovimiento(pila11[-1], pila4[-1]):
                    pila4.append(pila11.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 5:
                if validarMovimiento(pila11[-1], pila5[-1]):
                    pila5.append(pila11.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 6:
                if validarMovimiento(pila11[-1], pila6[-1]):
                    pila6.append(pila11.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 7:
                if validarMovimiento(pila11[-1], pila7[-1]):
                    pila7.append(pila11.pop())
                else:
                    print("No puedes poner esta carta")
            elif pilaDestino == 8:
                if pila11[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila11[-1] == "1♣":
                            pila8.append(pila11.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila11[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila8.append(pila11.pop())
                        else:
                            print("Carta no es la siguiente")
            elif pilaDestino == 9:
                if pila11[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila11[-1] == "1♦":
                            pila9.append(pila11.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila11[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila9.append(pila11.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila11[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila11[-1] == "1♥":
                            pila10.append(pila11.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila11[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            pila10.append(pila11.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")

#recorrer baraja y que cuando se acabe las cartas se reinicie la baraja
def recorrerBaraja():
    global baraja #se declara la variable global
    global pila12 #se declara la variable global
    if len(baraja) == 0: #si la baraja esta vacia
        for i in range(len(pila12)): #recorrer la pila12
            baraja.append(pila12.pop()) #agregar las cartas de la pila12 a la baraja
    else: #si la baraja no esta vacia
        pila12.append(baraja.pop()) #agregar la carta de la baraja a la pila12

#mover varias cartas
def moverCartas():
    global pila1
    global pila2
    global pila3
    global pila4
    global pila5
    global pila6
    global pila7
    global pila8
    global pila9
    global pila10
    global pila11
    global pila12
    global pilaOrigen
    global pilaDestino
    global baraja
    pila13 = []
    try:
        pilaOrigen = int(input("Pila origen: ")) #se pide la pila de origen
        pilaDestino = int(input("Pila destino: ")) #se pide la pila de destino
        nCartas = int(input("Numero de cartas: ")) #se pide el numero de cartas a mover
    except ValueError:
        print("Solo numeros")
        print("desea volver a intentar? (s/n)") #pregunta si desea continuar
        if input() == "s":
            return moverCartas() #vuelve a preguntar las pilas de origen y destino
        else:
            return mostrarMenu(intentos) #si no desea continuar vuelve al menu

    if pilaOrigen == 1: #si la pila de origen es 1
        if len(pila1) == 0: #si la pila esta vacia
            print("No hay cartas para mover") #se imprime que no hay cartas para mover
            return moverCartas() #se llama a la funcion moverCartas para volver a preguntar
        if nCartas > len(pila1): #si el numero de cartas es mayor al numero de cartas en la pila
            print("No hay tantas cartas en la pila")
        else:
            if pilaDestino == 2: #si la pila de destino es 2
                for i in range(nCartas): #recorrer el numero de cartas a mover
                        pila13.append(pila1.pop())
                for i in range(nCartas):
                    pila2.append(pila13.pop())
                        #pila2 = pila2 + pila1[range-nCartas:]  #agregar las cartas a la pila2
                        #pila1 = pila1[range:-nCartas] #eliminar las cartas de la pila1
            elif pilaDestino == 3:
                for i in range(nCartas):
                        pila13.append(pila1.pop())
                for i in range(nCartas):
                    pila3.append(pila13.pop())
            elif pilaDestino == 4:
                for i in range(nCartas):
                        pila13.append(pila1.pop())
                for i in range(nCartas):
                    pila4.append(pila13.pop())
            elif pilaDestino == 5:
                for i in range(nCartas):
                        pila13.append(pila1.pop())
                for i in range(nCartas):
                    pila5.append(pila13.pop())
            elif pilaDestino == 6:
                for i in range(nCartas):
                        pila13.append(pila1.pop())
                for i in range(nCartas):
                    pila6.append(pila13.pop())
            elif pilaDestino == 7:
                for i in range(nCartas):
                        pila13.append(pila1.pop())
                for i in range(nCartas):
                    pila7.append(pila13.pop())
            elif pilaDestino == 8:
                if pila1[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila1[-1] == "1♣":
                            for i in range(nCartas):
                                pila8.append(pila1.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila1[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila8.append(pila1.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila1[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila1[-1] == "1♦":
                            for i in range(nCartas):
                                pila9.append(pila1.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila1[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila9.append(pila1.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila1[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila1[-1] == "1♥":
                            for i in range(nCartas):
                                pila10.append(pila1.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila1[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila10.append(pila1.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila1[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila1[-1] == "1♠":
                            for i in range(nCartas):
                                pila11.append(pila1.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila1[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila11.append(pila1.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            else:
                print("No existe esa pila")
    elif pilaOrigen == 2:
        if len(pila2) == 0:
            print("No hay cartas para mover")
            return moverCartas()
        if nCartas > len(pila2): #si el numero de cartas es mayor al numero de cartas en la pila
            print("No hay tantas cartas en la pila")
        else:
            if pilaDestino == 1:
                for i in range(nCartas):
                        pila13.append(pila2.pop())
                for i in range(nCartas):
                            pila1.append(pila13.pop())
                    #if True: validarMovimiento(pila2[-1], pila1[-1] if len(pila1) != 0 else False):
                        #pila1.append(pila2.pop())
                    #else:
                        #print("No puedes poner esta carta")
                        #continue
            elif pilaDestino == 3:
                for i in range(nCartas):
                        pila13.append(pila2.pop())
                for i in range(nCartas):
                        pila3.append(pila13.pop())
                    #if True: validarMovimiento(pila2[-1], pila3[-1] if len(pila3) != 0 else False):
                        #pila3.append(pila2.pop())
                    #else:
                        #print("No puedes poner esta carta")
                        #continue
            elif pilaDestino == 4:
                for i in range(nCartas):
                        pila13.append(pila2.pop())
                for i in range(nCartas):
                        pila4.append(pila13.pop())
                    #if True: validarMovimiento(pila2[-1], pila4[-1] if len(pila4) != 0 else False):
                        #pila4.append(pila2.pop())
                    #else:
                        #print("No puedes poner esta carta")
                        #continue
            elif pilaDestino == 5:
                for i in range(nCartas):
                        pila13.append(pila2.pop())
                for i in range(nCartas):
                        pila5.append(pila13.pop())

                    #if True: validarMovimiento(pila2[-1], pila5[-1] if len(pila5) != 0 else False):
                        #pila5.append(pila2.pop())
                    #else:
                        #print("No puedes poner esta carta")
                        #continue
            elif pilaDestino == 6:
                for i in range(nCartas):
                        pila13.append(pila2.pop())
                for i in range(nCartas):
                        pila6.append(pila13.pop())

                    #if True: validarMovimiento(pila2[-1], pila6[-1] if len(pila6) != 0 else False):
                        #pila6.append(pila2.pop())
                    #else:
                        #print("No puedes poner esta carta")
                        #continue
            elif pilaDestino == 7:
                for i in range(nCartas):
                        pila13.append(pila2.pop())
                for i in range(nCartas):
                        pila7.append(pila13.pop())
                    #if True: validarMovimiento(pila2[-1], pila7[-1] if len(pila7) != 0 else False):
                        #pila7.append(pila2.pop())
                    #else:
                        #print("No puedes poner esta carta")
                        #continue
            elif pilaDestino == 8:
                if pila2[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila2[-1] == "1♣":
                            for i in range(nCartas):
                                pila8.append(pila2.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila2[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila8.append(pila2.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila2[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila2[-1] == "1♦":
                            for i in range(nCartas):
                                pila9.append(pila2.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila2[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila9.append(pila2.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila2[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila2[-1] == "1♥":
                            for i in range(nCartas):
                                pila10.append(pila2.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila2[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila10.append(pila2.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila2[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila2[-1] == "1♠":
                            for i in range(nCartas):
                                pila11.append(pila2.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila2[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila11.append(pila2.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            else:
                print("Pila no existe")
    elif pilaOrigen == 3:
        if len(pila3) == 0:
            print("No hay cartas para mover")
            return moverCartas()
        if nCartas > len(pila3): #si el numero de cartas es mayor al numero de cartas en la pila
            print("No hay tantas cartas en la pila")
        else:
            if pilaDestino == 1:
                for i in range(nCartas):
                        pila13.append(pila3.pop())
                for i in range(nCartas):
                            pila1.append(pila13.pop())
            elif pilaDestino == 2:
                for i in range(nCartas):
                        pila13.append(pila3.pop())
                for i in range(nCartas):
                    pila2.append(pila13.pop())
            elif pilaDestino == 4:
                for i in range(nCartas):
                        pila13.append(pila3.pop())
                for i in range(nCartas):
                    pila4.append(pila13.pop())
            elif pilaDestino == 5:
                for i in range(nCartas):
                        pila13.append(pila3.pop())
                for i in range(nCartas):
                    pila5.append(pila13.pop())
            elif pilaDestino == 6:
                for i in range(nCartas):
                        pila13.append(pila3.pop())
                for i in range(nCartas):
                    pila6.append(pila13.pop())
            elif pilaDestino == 7:
                for i in range(nCartas):
                        pila13.append(pila3.pop())
                for i in range(nCartas):
                    pila7.append(pila13.pop())
            elif pilaDestino == 8:
                if pila3[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila3[-1] == "1♣":
                            for i in range(nCartas):
                                pila8.append(pila3.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila3[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila8.append(pila3.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila3[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila3[-1] == "1♦":
                            for i in range(nCartas):
                                pila9.append(pila3.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila3[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila9.append(pila3.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila3[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila3[-1] == "1♥":
                            for i in range(nCartas):
                                pila10.append(pila3.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila3[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila10.append(pila3.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila3[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila3[-1] == "1♠":
                            for i in range(nCartas):
                                pila11.append(pila3.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila3[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila11.append(pila3.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            else:
                print("No existe esa pila")
    elif pilaOrigen == 4:
        if len(pila4) == 0:
            print("No hay cartas para mover")
            return moverCartas()
        if nCartas > len(pila4): #si el numero de cartas es mayor al numero de cartas en la pila
            print("No hay tantas cartas en la pila")
        else:
            if pilaDestino == 1:
                for i in range(nCartas):
                        pila13.append(pila4.pop())
                for i in range(nCartas):
                            pila1.append(pila13.pop())
            elif pilaDestino == 2:
                for i in range(nCartas):
                        pila13.append(pila4.pop())
                for i in range(nCartas):
                            pila2.append(pila13.pop())
            elif pilaDestino == 3:
                for i in range(nCartas):
                        pila13.append(pila4.pop())
                for i in range(nCartas):
                            pila3.append(pila13.pop())
            elif pilaDestino == 5:
                for i in range(nCartas):
                        pila13.append(pila4.pop())
                for i in range(nCartas):
                            pila5.append(pila13.pop())
            elif pilaDestino == 6:
                for i in range(nCartas):
                        pila13.append(pila4.pop())
                for i in range(nCartas):
                            pila6.append(pila13.pop())
            elif pilaDestino == 7:
                for i in range(nCartas):
                        pila13.append(pila4.pop())
                for i in range(nCartas):
                            pila7.append(pila13.pop())
            elif pilaDestino == 8:
                if pila4[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila4[-1] == "1♣":
                            for i in range(nCartas):
                                pila8.append(pila4.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila4[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila8.append(pila4.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila4[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila4[-1] == "1♦":
                            for i in range(nCartas):
                                pila9.append(pila4.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila4[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila9.append(pila4.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila4[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila4[-1] == "1♥":
                            for i in range(nCartas):
                                pila10.append(pila4.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila4[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila10.append(pila4.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila4[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila4[-1] == "1♠":
                            for i in range(nCartas):
                                pila11.append(pila4.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila4[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila11.append(pila4.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            else:
                print("No existe esa pila")
    elif pilaOrigen == 5:
        if len(pila5) == 0:
            print("No hay cartas para mover")
            return moverCartas()
        if nCartas > len(pila5): #si el numero de cartas es mayor al numero de cartas en la pila
            print("No hay tantas cartas en la pila")
        else:
            if pilaDestino == 1:
                for i in range(nCartas):
                        pila13.append(pila5.pop())
                for i in range(nCartas):
                    pila1.append(pila13.pop())
            elif pilaDestino == 2:
                for i in range(nCartas):
                        pila13.append(pila5.pop())
                for i in range(nCartas):
                    pila2.append(pila13.pop())
            elif pilaDestino == 3:
                for i in range(nCartas):
                        pila13.append(pila5.pop())
                for i in range(nCartas):
                    pila3.append(pila13.pop())
            elif pilaDestino == 4:
                for i in range(nCartas):
                        pila13.append(pila5.pop())
                for i in range(nCartas):
                    pila4.append(pila13.pop())
            elif pilaDestino == 6:
                for i in range(nCartas):
                        pila13.append(pila5.pop())
                for i in range(nCartas):
                    pila6.append(pila13.pop())
            elif pilaDestino == 7:
                for i in range(nCartas):
                        pila13.append(pila5.pop())
                for i in range(nCartas):
                    pila7.append(pila13.pop())
            elif pilaDestino == 8:
                if pila5[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila5[-1] == "1♣":
                            for i in range(nCartas):
                                pila8.append(pila5.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila5[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila8.append(pila5.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila5[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila5[-1] == "1♦":
                            for i in range(nCartas):
                                pila9.append(pila5.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila5[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila9.append(pila5.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila5[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila5[-1] == "1♥":
                            for i in range(nCartas):
                                pila10.append(pila5.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila5[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila10.append(pila5.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila5[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila5[-1] == "1♠":
                            for i in range(nCartas):
                                pila11.append(pila5.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila5[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila11.append(pila5.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            else:
                print("No existe esa pila")
    elif pilaOrigen == 6:
        if len(pila6) == 0:
            print("No hay cartas para mover")
            return moverCartas()
        if nCartas > len(pila6): #si el numero de cartas es mayor al numero de cartas en la pila
            print("No hay tantas cartas en la pila")
        else:
            if pilaDestino == 1:
                for i in range(nCartas):
                        pila13.append(pila6.pop())
                for i in range(nCartas):
                    pila1.append(pila13.pop())
            elif pilaDestino == 2:
                for i in range(nCartas):
                        pila13.append(pila6.pop())
                for i in range(nCartas):
                    pila2.append(pila13.pop())
            elif pilaDestino == 3:
                for i in range(nCartas):
                        pila13.append(pila6.pop())
                for i in range(nCartas):
                    pila3.append(pila13.pop())
            elif pilaDestino == 4:
                for i in range(nCartas):
                        pila13.append(pila6.pop())
                for i in range(nCartas):
                    pila4.append(pila13.pop())
            elif pilaDestino == 5:
                for i in range(nCartas):
                        pila13.append(pila6.pop())
                for i in range(nCartas):
                    pila5.append(pila13.pop())
            elif pilaDestino == 7:
                for i in range(nCartas):
                        pila13.append(pila6.pop())
                for i in range(nCartas):
                    pila7.append(pila13.pop())
            elif pilaDestino == 8:
                if pila6[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila6[-1] == "1♣":
                            for i in range(nCartas):
                                pila8.append(pila6.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila6[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila8.append(pila6.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila6[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila6[-1] == "1♦":
                            for i in range(nCartas):
                                pila9.append(pila6.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila6[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila9.append(pila6.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila6[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila6[-1] == "1♥":
                            for i in range(nCartas):
                                pila10.append(pila6.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila6[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila10.append(pila6.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila6[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila6[-1] == "1♠":
                            for i in range(nCartas):
                                pila11.append(pila6.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila6[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila11.append(pila6.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            else:
                print("Pila no existe")
    elif pilaOrigen == 7:
        if len(pila7) == 0:
            print("No hay cartas para mover")
            return moverCartas()
        if nCartas > len(pila7): #si el numero de cartas es mayor al numero de cartas en la pila
            print("No hay tantas cartas en la pila")
        else:
            if pilaDestino == 1:
                for i in range(nCartas):
                        pila13.append(pila7.pop())
                for i in range(nCartas):
                    pila1.append(pila13.pop())
            elif pilaDestino == 2:
                for i in range(nCartas):
                        pila13.append(pila7.pop())
                for i in range(nCartas):
                    pila2.append(pila13.pop())
            elif pilaDestino == 3:
                for i in range(nCartas):
                        pila13.append(pila7.pop())
                for i in range(nCartas):
                    pila3.append(pila13.pop())
            elif pilaDestino == 4:
                for i in range(nCartas):
                        pila13.append(pila7.pop())
                for i in range(nCartas):
                    pila4.append(pila13.pop())
            elif pilaDestino == 5:
                for i in range(nCartas):
                        pila13.append(pila7.pop())
                for i in range(nCartas):
                    pila5.append(pila13.pop())
            elif pilaDestino == 6:
                for i in range(nCartas):
                        pila13.append(pila7.pop())
                for i in range(nCartas):
                    pila6.append(pila13.pop())
            elif pilaDestino == 8:
                if pila7[-1][-1] == "♣":
                    if len (pila8) == 0:
                        if pila7[-1] == "1♣":
                            for i in range(nCartas):
                                pila8.append(pila7.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♣ de primera carta")
                    else:
                        value0 = pila7[-1][0]
                        value1 = pila8[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila8.append(pila7.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 9:
                if pila7[-1][-1] == "♦":
                    if len (pila9) == 0:
                        if pila7[-1] == "1♦":
                            for i in range(nCartas):
                                pila9.append(pila7.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♦ de primera carta")
                    else:
                        value0 = pila7[-1][0]
                        value1 = pila9[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila9.append(pila7.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 10:
                if pila7[-1][-1] == "♥":
                    if len (pila10) == 0:
                        if pila7[-1] == "1♥":
                            for i in range(nCartas):
                                pila10.append(pila7.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♥ de primera carta")
                    else:
                        value0 = pila7[-1][0]
                        value1 = pila10[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila10.append(pila7.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            elif pilaDestino == 11:
                if pila7[-1][-1] == "♠":
                    if len (pila11) == 0:
                        if pila7[-1] == "1♠":
                            for i in range(nCartas):
                                pila11.append(pila7.pop())
                        else:
                            print("No puedes poner una carta de diferente 1♠ de primera carta")
                    else:
                        value0 = pila7[-1][0]
                        value1 = pila11[-1][0]
                        if value0 == 'K':
                            value0 = 13
                        elif value0 == 'Q':
                            value0 = 12
                        elif value0 == 'J':
                            value0 = 11
                        else:
                            value0 = int(value0)
                        if value1 == 'K':
                            value1 = 13
                        elif value1 == 'Q':
                            value1 = 12
                        elif value1 == 'J':
                            value1 = 11
                        else:
                            value1 = int(value1)
                        
                        if value1 == value0 - 1:
                            for i in range(nCartas):
                                pila11.append(pila7.pop())
                        else:
                            print("Carta no es la siguiente")
                else:
                    print("no puedes poner esta carta")
            else:
                print("No existe esa pila")

#Reiniciar juego
def jugarDeNuevo(): # bacia las pilas
    global baraja
    global pila1
    global pila2
    global pila3
    global pila4
    global pila5
    global pila6
    global pila7
    global pila8
    global pila9
    global pila10
    global pila11
    global pila12
    baraja = []
    pila1 = []
    pila2 = []
    pila3 = []
    pila4 = []
    pila5 = []
    pila6 = []
    pila7 = []
    pila8 = []
    pila9 = []
    pila10 = []
    pila11 = []
    pila12 = []
    crearBaraja() #crea la baraja de nuevo
    repartir() #reparte las cartas de nuevo

#menu
def mostrarMenu(intentos): #muestra el menu
    os.system("cls") #limpia la pantalla
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━❪ ＢＩＥＮＶＥＮＩＤＯ ❫━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    if not intentos: #si no hay intentos
        print(" ")
        print("                                 PRESIONA 0 PARA JUGAR")
        print(" ")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") 
    if intentos: #si hay intentos
        print(" Baraja: ", "'?'","                                                     JUGADOR: "+nombre) #muestra el jugador
        print(" Tomar0: ", pila12,)
        print("" )                   
        print(" mano1: ", pila1) 
        print(" mano2: ", pila2)
        print(" mano3: ", pila3)
        print(" mano4: ", pila4)
        print(" mano5: ", pila5)
        print(" mano6: ", pila6)
        print(" mano7: ", pila7)
        print(" ")
        print(" 8  ♣: ", pila8)
        print(" 9  ♦: ", pila9)
        print(" 10 ♥: ", pila10)
        print(" 11 ♠: ", pila11)
        print(" ")
        print("  ╔════════════════╗ ")
        print("  ║1. Mover carta  ║ ")
        print("  ║2. Tomar carta  ║ ")
        print("  ║3. Mover varias ║ ")
        print("  ║4. Rendirse     ║ ")
        print("  ║5. Como jugar   ║ ")
        print("  ║6. Estadisticas ║ ")
        print("  ║7. Salir        ║ ")
        print("  ╚════════════════╝ ")    
        

    # mostrar si gana
    if len([pila8, pila9, pila10, pila11]) == 13: #si las pilas 8,9,10,11 tienen 13 cartas
        ganadas += 1 #aumenta las ganadas
        print("Ganaste") #muestra que ganaste
        file = open("puntaje.txt", "w") #abre el archivo
        file.write("Ganaste") #escribe ganaste
        file.write("Total ganadas: " + str(ganadas)) #escribe las ganadas
        file.write("Total perdidas: " + str(perdidas)) #escribe las perdidas
        file.close() #cierra el archivo
        print("Desea jugar de nuevo? (s/n)") #pregunta si quiere jugar de nuevo
        respuesta = input() #lee la respuesta
        if respuesta == "s": #si la respuesta es s
            jugarDeNuevo() #reinicia el juego
        else: #si no
            exit() #sale del juego
    elif len(pila8) >= 14: #si la pila 8 tiene mas de 14 cartas
        print("No puedes poner mas de 13 cartas en una pila♣")
    elif len(pila9) >= 14:
        print("No puedes poner mas de 13 cartas en una pila♦")
    elif len(pila10) >= 14:
        print("No puedes poner mas de 13 cartas en una pila♥")
    elif len(pila11) >= 14:
        print("No puedes poner mas de 13 cartas en una pila♠")


# programa principal
crearBaraja() #crea la baraja
intentos = False #no hay intentos
while True: #mientras sea verdadero
    mostrarMenu(intentos) #muestra el menu
    print(" ")
    try: #intenta
        opcion = int(input(" opcion: ")) #lee la opcion
    except ValueError: #si hay un error
        print("Ingrese un numero") #muestra que ingrese un numero
        continue #continua
    if opcion == 0: #si la opcion es 0
        if intentos: #si hay intentos
            print(" ")
        else: #si no
            intentos = True #hay intentos
            print("Dijite su nombre: ") #pide el nombre
            nombre = input() #lee el nombre
            repartir() #reparte las cartas
    elif opcion == 1: #si la opcion es 1
        moverPilas()
    elif opcion == 2: #si la opcion es 2
        recorrerBaraja() 
    elif opcion == 3: #si la opcion es 3
        moverCartas()
    elif opcion == 4: #si la opcion es 4
        print("Perdiste") #muestra que perdiste
        perdidas += 1 #aumenta las perdidas
        file = open("puntaje.txt", "a") #file = open("nombre doc", "w para sobreescribir y a para agregar permanente") 
        file.write(nombre) #escribe el nombre
        file.write(": Total ganadas: " + str(ganadas) ) #escribe las ganadas
        file.write(" Total perdidas: " + str(perdidas)) #escribe las perdidas
        file.write("\n") #salto de linea
        file.close() #cierra el archivo
        print("Desea jugar de nuevo? (s/n)") #pregunta si quiere jugar de nuevo
        respuesta = input() #lee la respuesta
        if respuesta == "s": #si la respuesta es s
            jugarDeNuevo()
        else: #si no
            exit() #sale del juego
        jugarDeNuevo()
    elif opcion == 5:
        print(" ")
        print("  ╔════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗ ")
        print("  ║1. El objetivo del juego es colocar todas las cartas en las pilas 8,9,10,11 en su orden acendente.   1=As       ║ ")
        print("  ║       ejemplo:  8♣: 1♣,2♣,3♣,4♣,5♣,6♣,7♣,8♣,9♣,10♣,J♣,Q♣,K♣                                                    ║ ")
        print("  ║2. Para mover una carta, debes seleccionar la opcion 1 y escoger la pila de origen y la pila de destino.        ║ ")
        print("  ║       pila de origen: donde esta la carta que quieres mover                                                    ║ ")
        print("  ║       pila de destino: a donde quieres que este la carta que estas moviendo                                    ║ ")
        print("  ║3. Para mover varias cartas, debes seleccionar la opcion 3                                                      ║ ")
        print("  ║4. Para tomar una carta, debes seleccionar la opcion 2 y la carta tomara una carta de la baraja, puedes hacer   ║ ")
        print("  ║  esto varias veces para recorrer la baraja                                                                     ║ ")
        print("  ║5. Para rendirse, debes seleccionar la opcion 4.                                                                ║ ")
        print("  ║6. Para mostrar estadisticas, debes seleccionar la opcion 6.                                                    ║ ")
        print("  ║7. Para salir, debes seleccionar la opcion 7.                                                                   ║ ")
        print("  ║                                                                                                                ║ ")
        print("  ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝ ")
        print(" ")
        print("Presione enter para volver al menu")
        input()
    elif opcion == 6:
        file = open("puntaje.txt")
        print(file.read())
        file.close()
        print("Presione enter para volver al menu")
    elif opcion == 7:   
        break
    else:
        print("Opcion incorrecta")
    input("Pulse enter para continuar...")
