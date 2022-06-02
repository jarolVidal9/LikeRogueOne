import numpy as np
import random
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
def ImportarMapa():
    aleatorio=random.randint(1,6)
    if aleatorio==1:
        print("Mapa 1")
        archivo= open('Mapas//Mapa1.txt',"r")
    if aleatorio==2:
        print("Mapa 2")
        archivo= open('Mapas//Mapa2.txt',"r")
    if aleatorio==3:
        print("Mapa 3")
        archivo= open('Mapas//Mapa3.txt',"r")
    if aleatorio==4:
        print("Mapa 4")
        archivo= open('Mapas//Mapa4.txt',"r")
    if aleatorio==5:
        print("Mapa 5")
        archivo= open('Mapas//Mapa5.txt',"r")
    if aleatorio==6:
        print("Mapa 6")
        archivo= open('Mapas//Mapa6.txt',"r")
    Lista=[]
    for linea in archivo.readlines():
        Lista.append(Convert(linea))
    archivo.close()
    return Lista
def CordenadasMuros(Lista):
    Cordenadas=[]
    i1=0
    j1=0
    for i in Lista:
        for j in i:
            if j=='1':
                Cordenadas.append([i1,j1])
            j1+=1
        j1=0
        i1+=1
    return Cordenadas
def CordenadasFondo(Lista):
    Cordenadas=[]
    i1=0
    j1=0
    for i in Lista:
        for j in i:
            if j=='0':
                Cordenadas.append([i1,j1])
            j1+=1
        j1=0
        i1+=1
    return Cordenadas
def CordenadasPiso(Lista):
    Cordenadas=[]
    i1=0
    j1=0
    for i in Lista:
        for j in i:
            if j=='.':
                Cordenadas.append([i1,j1])
            j1+=1
        j1=0
        i1+=1
    return Cordenadas
def PosicionEnemigos(CordenadasPiso):
    CantidadEnemigos=10
    CordenadasEnemigos=[]
    for i in range(CantidadEnemigos):
        pos=random.randint(0,len(CordenadasPiso)-1)
        CordenadasEnemigos.append(CordenadasPiso[pos])
    return CordenadasEnemigos
def PuntoSalida(CordenadasPiso):
    Ciclo=True
    while Ciclo:
        pos=random.randint(0,len(CordenadasPiso)-1)
        print("Punto salida:",CordenadasPiso[pos][0]/50," ",CordenadasPiso[pos][1]/50)
        if CordenadasPiso[pos][0]/50>15 and CordenadasPiso[pos][1]/50>15:
            Ciclo=False
            return CordenadasPiso[pos]

def PuntosPotenciadores(CordenadasPiso):
    CantidadPotenciadores=2
    CordenadasPotenciadores=[]
    for i in range(CantidadPotenciadores):
        pos=random.randint(0,len(CordenadasPiso)-1)
        CordenadasPotenciadores.append(CordenadasPiso[pos])
    return CordenadasPotenciadores
