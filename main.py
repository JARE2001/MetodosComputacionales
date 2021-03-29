from Acomentarios import *
from Avariables import *
from AReales import *
from AEnteros import *


Aent = AutomataEntero()
Areal = AutomataReal()
Avar = AutomataVariable()
Acom = AutomataComentario()


def lexerAritmetico(inputU):
    f = open(inputU, "r")
    for x in f:
        i = 0
        while i < len(x):
            if( -1 != Acom.processEntry(x, i) ):
                accepted = Acom.processEntry(x, i)
                print(x[i:accepted], "      |comment")
                i = accepted
            elif( -1 != Avar.processEntry(x, i) ):
                accepted = Avar.processEntry(x, i)
                print(x[i:accepted], "                      |variable")
                i = accepted
            elif( -1 != Areal.processEntry(x, i) ):
                accepted = Areal.processEntry(x, i)
                print(x[i:accepted], "                      |real")
                i = accepted
            elif( -1 != Aent.processEntry(x, i) ):
                accepted = Aent.processEntry(x, i)
                print(x[i:accepted], "                      |entero")
                i = accepted
            elif(x[i] == "="):
                print("=                        |asignacion")
                i+=1
            elif(x[i] == "+"):
                print("+                        |suma")
                i+=1
            elif(x[i] == "-"):
                print("-                        |resta")
                i+=1
            elif(x[i] == "*"):
                print("*                        |multiplicacion")
                i+=1
            elif(x[i] == "/"):
                print("/                        |division")
                i+=1
            elif(x[i] == "^"):
                print("^                        |potencia")
                i+=1
            elif(x[i] == "("):
                print("(                        |parentesis izquierdo")
                i+=1
            elif(x[i] == ")"):
                print(")                        |parentesis derecho")
                i+=1
            else:
                i+=1  

#main

inputU =input("Que archivo quieres leer?    ")

lexerAritmetico(inputU)
