class AutomataEntero:
    def __init__(self):
        self.state = 0

    def state0(self,c):
        if(c.isdigit()):
            self.state = 2
        elif(c == "-"):
            self.state =1
        else:
            self.state = -1
    def state1(self,c):
        if(c.isdigit()):
            self.state = 2
        else:
            self.state = -1
    def state2(self,c):
        if(c.isdigit()):
            self.state = 2
        else:
            self.state = -2

    def processEntry(self,cadena,i):
        self.__init__()
        while(not self.state == -2 and not self.state == -1 and i < len(cadena)):
            if (self.state == 0):
                self.state0(cadena[i])
            elif (self.state == 1):
                self.state1(cadena[i])
            elif (self.state == 2):
                self.state2(cadena[i]) 
            i+=1    
        if(self.state == 2 ):
            return i
        elif(self.state == -2):
            return i-1
        else:
            return -1