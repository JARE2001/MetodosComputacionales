class AutomataVariable:
    def __init__(self):
        self.state = 0

    def state0(self,c):
        if(c.isalpha()):
            self.state = 1
        else:
            self.state = -1
    def state1(self,c):
        if(c.isalpha() or c == "_" or c.isdigit()):
            self.state = 1
        else:
            self.state = -1

    def processEntry(self,cadena,i):
        estadoI =i+1
    
        while(not self.state == -1 and i < len(cadena)):
            if (self.state == 0):
                self.state0(cadena[i])
            elif (self.state == 1):
                self.state1(cadena[i]) 
            i+=1    
        if(i <= estadoI):
            print("La cadena no contiene una variable")
        else:
            print(cadena[0:i-1])
            print("La cadena contine una variable")
        self.state = 0
        return i-1