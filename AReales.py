class AutomataReal:
    def __init__(self):
        self.state = 0

    def state0(self,c):
        if(c.isdigit()):
            self.state = 1
        elif(c == "-"):
            self.state = 2
        elif(c == "."):
            self.state = 3
        else:
            self.state = -1
    def state1(self,c):
        if(c.isdigit()):
            self.state = 1
        elif(c == "."):
            self.state = 4
        else:
            self.state = -1
        
    def state2(self,c):  
        if(c.isdigit()):
            self.state = 1
        elif(c == "."):
            self.state = 3
        else:
            self.state = -1

    def state3(self,c):
        if(c.isdigit()):
            self.state = 5
        else:
            self.state = -1

    def state4(self,c):
        if(c.isdigit()):
            self.state = 5
        else:
            self.state = -1   

    def state5(self,c):   
        if(c.isdigit()):
            self.state = 5
        elif(c == "E" or c == "e"):
            self.state = 6
        else:
            self.state = -1  

    def state6(self,c):
        if(c.isdigit()):
            self.state = 7
        elif(c == "-"):
            self.state = 8   
        else:
            self.state = -1      

    def state7(self,c):  
        if(c.isdigit()):
            self.state = 7
        else:
            self.state = -1
            
    def state8(self,c):    
        if(c.isdigit()):
                self.state = 7
        else:
            self.state = -1
                        

    def processEntry(self,cadena,i):
        estadoI =i+1
        while(not self.state == -1 and i < len(cadena)):
            if (self.state == 0):
                self.state0(cadena[i])
            elif (self.state == 1):
                self.state1(cadena[i])
            elif (self.state == 2):
                self.state2(cadena[i])
            elif (self.state == 3):
                self.state3(cadena[i])
            elif (self.state == 4):
                self.state4(cadena[i])
            elif (self.state == 5):
                self.state5(cadena[i])
            elif (self.state == 6):
                self.state6(cadena[i])
            elif (self.state == 7):
                self.state7(cadena[i])
            elif (self.state == 8):
                self.state8(cadena[i])
            i+=1    
        if(i <= estadoI):
            print("La cadena no contiene un Real")
        else:
            print(cadena[0:i-1])
            print("La cadena contine un Real")
        self.state = 0
        return i-1