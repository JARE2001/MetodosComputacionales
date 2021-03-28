class AutomataComentario:
    def __init__(self):
        self.state = 0

    def state0(self,c):
        if(c =="/"):
            self.state = 1
        else:
            self.state = -1

    def state1(self,c):
        if(c =="/"):
            self.state = 2
        else:
            self.state = -1

    def state2(self,c):
        self.state = 2

    def processEntry(self,cadena,i):
        estadoI =i+1
        while(not self.state == -1 and i < len(cadena)):
            if (self.state == 0):
                self.state0(cadena[i])
            elif (self.state == 1):
                self.state1(cadena[i])
            elif (self.state == 2):
                self.state2(cadena[i])
            i+=1    
        if(i <= estadoI):
            print("La cadena no contiene una comentario")
        else:
            print(cadena[0:i-1])
            print("La cadena contine un comentario")
        self.state = 0
        return i-1 
