class AutomataOperador:
    
    def processEntry(self,cadena,i):
        if(cadena[i] == "="):
            print("asignacion")
            return i+1
        elif(cadena[i] == "+"):
            print("suma")
            return i+1
        elif(cadena[i] == "-"):
            print("resta")
            return i+1
        elif(cadena[i] == "*"):
            print("multiplicacion")
            return i+1
        elif(cadena[i] == "/"):
            print("division")
            return i+1
        elif(cadena[i] == "/"):
            print("potencia")
            return i+1
        elif(cadena[i] == "("):
            print("parentesis izquirdo")
            return i+1
        elif(cadena[i] == ")"):
            print("parentecis derecho")
            return i+1
        else:
            return i+1