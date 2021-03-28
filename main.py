from Acomentarios import *
from Avariables import *
from AReales import *
from AEnteros import *
from Aoperadores import *

# a = AutomataComentario()
# a.processEntry("jorge//(68608608         Jorge",5)

# a = AutomataVariable()
# a.processEntry("j000",0)

#a = AutomataReal()
#a.processEntry("2.3E3",0)
#a.processEntry("6.345e-5",0)
#a.processEntry("-0.001E-3",0)
#a.processEntry(".467E9",0)

# a = AutomataEntero()
# a.processEntry("23",0)

Aent = AutomataEntero()
Areal = AutomataReal()
Avar = AutomataVariable()
Acom = AutomataComentario()
Aop = AutomataOperador()

Automatas = [Aent,Areal,Acom,Avar,Aop]


f = open("input1.txt", "r")
for x in f:
    i = 0
    while i < len(x):
        for j in range(5):
            i = Automatas[j].processEntry(x,i)
        print(x[i:])

    #print(x,end="")