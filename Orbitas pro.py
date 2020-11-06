# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:23:25 2020

@author: facun
"""
import matplotlib.pyplot as plt
import random
import numpy as np
import imageio
# =============================================================================
# Lista de datos inciales
# =============================================================================
datos=["x0","vel_orb","masa","periodo"]
sol=[0.0 ,0.0,1.98e30, 0.0]
mercurio=[46001009.0 ,47.362*1000 ,0.330114e24 ,87.96934]
venus=[107476170.0 ,35.02*1000 ,4.8690e24 ,87.96934]
tierra=[147098291.0 ,29.79*1000 ,5.9742e24 ,365]
marte= [380951528.0 ,24.07*1000 ,6.4191e23 ,700]
jupiter=[740679835.0 ,13.05*1000 ,1898.187e24 ,87.96934]
saturno=[1349823615.0 ,9.64*1000 ,568.3174e24 ,87.96934]
urano=[2734998229.0 ,6.81*1000 ,86.8127e24 ,87.96934]
neptuno=[4452940833.0 ,5.43*1000 ,102.4126e24 ,87.96934]
pluton=[4436756954.0 ,4.72*1000 ,0.013030e24 ,87.96934]
G = 6.693e-11
dt= 24*60*60*7

planetax=("pos_solx","pos_mercuriox","pos_venusx","pos_tierrax","pos_martex","pos_jupiterx","pos_saturnox","pos_uranox","pos_neptunox","pos_plutonx")
planetay=("pos_soly","pos_mercurioy","pos_venusy","pos_tierray","pos_martey","pos_jupitery","pos_saturnoy","pos_uranoy","pos_neptunox","pos_plutony")
# =============================================================================
# Lista de pos iniciales
# =============================================================================
pos_sol=[(0.0,0.0)]
pos_mercurio=[(46001009.0,0.0)]
pos_venus=[(107476170.0,0.0)]
pos_tierra=[(147098291.0,0.0)]
pos_marte=[(380951528.0,0.0)]
pos_jupiter=[(740679835.0,0.0)]
pos_saturno=[(1349823615.0,0.0)]
pos_urano=[(2734998229.0,0.0)]
pos_neptuno=[(4459753056.0,0.0)]
pos_pluton=[(4436756954.0,0.0)]
pos_solx=[00.0,00.0]

pos_mercuriox=[46001009000.0,46001009000.0]
pos_venusx=   [107476170000.0,107476170000.0]
pos_tierrax=  [147095000000.0,147098291000.0]
pos_martex=   [249209300000.0,249209300000.0]
pos_jupiterx= [740679835000.0,740679835000.0]
pos_saturnox= [1434000000000.0,1434000000000.0]
pos_uranox=   [2734998229000.0,2734998229000.0]
pos_neptunox= [4459753056000.0,4459753056000.0]
pos_plutonx=  [4436756954000.0,4436756954000.0]
 #=============================================================================
pos_soly=[0.0,0.0]
pos_mercurioy=[0.0,(mercurio[1]*dt)]
pos_venusy=[0.0,(venus[1]*dt)]
pos_tierray=[0.0,(tierra[1]*dt)]
pos_martey=[0.0,(marte[1]*dt)]
pos_jupitery=[0.0,(jupiter[1]*dt)]
pos_saturnoy=[0.0,(saturno[1]*dt)]
pos_uranoy=[0.0,(urano[1]*dt)]
pos_neptunoy=[0.0,(neptuno[1]*dt)]
pos_plutony=[0.0,(pluton[1]*dt)]

#posiciones_x=[pos_solx[0],pos_mercuriox[0],pos_venusx[0],pos_tierrax[0],pos_martex[0],pos_jupiterx[0],pos_saturnox[0],pos_uranox[0],pos_neptunox[0],pos_plutonx[0]]
#posiciones_y=[pos_soly[0],pos_mercurioy[0],pos_venusy[0],pos_tierray[0],pos_martey[0],pos_jupitery[0],pos_saturnoy[0],pos_uranoy[0],pos_neptunoy[0],pos_plutony[0]]
masas=[sol[2],mercurio[2],venus[2],tierra[2],marte[2],jupiter[2],saturno[2],urano[2],neptuno[2],pluton[2]]

# =============================================================================
# bloques de calculos
# =============================================================================

def calcular_delta(pos1,pos2):
    delta=(pos1-pos2)
    return delta

def dis_trigo(disx,disy):
    d=np.sqrt(disx**2+disy**2)
    return d

def realiza_verlet(pos_anterior,pos_actual,aceleracion_actual):
    d1=pos_anterior
    d2=pos_actual
    a=aceleracion_actual
    siguiente_pos=2*d2-d1+a*(dt*dt)
    return siguiente_pos

def calcular_fuerza(posicionx1,posicionx2,posiciony1,posiciony2,masa1,masa2):
    dx=calcular_delta(posicionx1,posicionx2)
    dy=calcular_delta(posiciony1,posiciony2)
    d=dis_trigo(dx,dy)
    fuerza=(G*masa1*masa2)/(d**2)
    fuerzax=fuerza*(dx/d)
    fuerzay=fuerza*(dy/d)
    return fuerzax,fuerzay

def calcular_fuerza_total(numero_planeta,k):
    posiciones_x=[pos_solx[0],pos_mercuriox[k],pos_venusx[k],pos_tierrax[k],pos_martex[k],pos_jupiterx[k],pos_saturnox[k],pos_uranox[k],pos_neptunox[k],pos_plutonx[k]]
    posiciones_y=[pos_soly[0],pos_mercurioy[k],pos_venusy[k],pos_tierray[k],pos_martey[k],pos_jupitery[k],pos_saturnoy[k],pos_uranoy[k],pos_neptunoy[k],pos_plutony[k]]
    fuerzasx=0
    fuerzasy=0
    for i in range(len(posiciones_x)):
        if i!=numero_planeta:
            fuerza=calcular_fuerza(posiciones_x[i],posiciones_x[numero_planeta],posiciones_y[i],posiciones_y[numero_planeta],masas[i],masas[numero_planeta])
            fuerzasx=fuerzasx+fuerza[0]
            fuerzasy=fuerzasy+fuerza[1]
    return fuerzasx,fuerzasy

def calcular_aceleraciones (numero_planeta,k):
    fuerzas_total=calcular_fuerza_total(numero_planeta,k)
    aceleacion_x=fuerzas_total[0]/masas[numero_planeta]
    aceleacion_y=fuerzas_total[1]/masas[numero_planeta]
    return aceleacion_x,aceleacion_y

def ciclo(t):
    posiciones_x=[pos_solx[0],pos_mercuriox[t],pos_venusx[t],pos_tierrax[t],pos_martex[t],pos_jupiterx[t],pos_saturnox[t],pos_uranox[t],pos_neptunox[t],pos_plutonx[t]]
    posiciones_y=[pos_soly[0],pos_mercurioy[t],pos_venusy[t],pos_tierray[t],pos_martey[t],pos_jupitery[t],pos_saturnoy[t],pos_uranoy[t],pos_neptunoy[t],pos_plutony[t]]
    posiciones_anteriores_x=[pos_solx[0],pos_mercuriox[t-1],pos_venusx[t-1],pos_tierrax[t-1],pos_martex[t-1],pos_jupiterx[t-1],pos_saturnox[t-1],pos_uranox[t-1],pos_neptunox[t-1],pos_plutonx[t-1]]
    posiciones_anteriores_y=[pos_soly[0],pos_mercurioy[t-1],pos_venusy[t-1],pos_tierray[t-1],pos_martey[t-1],pos_jupitery[t-1],pos_saturnoy[t-1],pos_uranoy[t-1],pos_neptunoy[t-1],pos_plutony[t-1]]
    for numero_planeta in range (1,10):
        ax=calcular_aceleraciones(numero_planeta,t)[0]
        ay=calcular_aceleraciones(numero_planeta,t)[1]
        if numero_planeta==1:
            x=realiza_verlet(posiciones_anteriores_x[1],posiciones_x[1],ax)
            y=realiza_verlet(posiciones_anteriores_y[1],posiciones_y[1],ay)
            pos_mercuriox.append(x)
            pos_mercurioy.append(y)
        if numero_planeta==2:
            x=realiza_verlet(posiciones_anteriores_x[2],posiciones_x[2],ax)
            y=realiza_verlet(posiciones_anteriores_y[2],posiciones_y[2],ay)
            pos_venusx.append(x)
            pos_venusy.append(y)
        if numero_planeta==3:
            x=realiza_verlet(posiciones_anteriores_x[3],posiciones_x[3],ax)
            y=realiza_verlet(posiciones_anteriores_y[3],posiciones_y[3],ay)
            pos_tierrax.append(x)
            pos_tierray.append(y)
        if numero_planeta==4:
            x=realiza_verlet(posiciones_anteriores_x[4],posiciones_x[4],ax)
            y=realiza_verlet(posiciones_anteriores_y[4],posiciones_y[4],ay)
            pos_martex.append(x)
            pos_martey.append(y)
        if numero_planeta==5:
            x=realiza_verlet(posiciones_anteriores_x[5],posiciones_x[5],ax)
            y=realiza_verlet(posiciones_anteriores_y[5],posiciones_y[5],ay)
            pos_jupiterx.append(x)
            pos_jupitery.append(y)
        if numero_planeta==6:
            x=realiza_verlet(posiciones_anteriores_x[6],posiciones_x[6],ax)
            y=realiza_verlet(posiciones_anteriores_y[6],posiciones_y[6],ay)
            pos_saturnox.append(x)
            pos_saturnoy.append(y)
        if numero_planeta==7:
            x=realiza_verlet(posiciones_anteriores_x[7],posiciones_x[7],ax)
            y=realiza_verlet(posiciones_anteriores_y[7],posiciones_y[7],ay)
            pos_uranox.append(x)
            pos_uranoy.append(y)
        if numero_planeta==8:
            x=realiza_verlet(posiciones_anteriores_x[8],posiciones_x[8],ax)
            y=realiza_verlet(posiciones_anteriores_y[8],posiciones_y[8],ay)
            pos_neptunox.append(x)
            pos_neptunoy.append(y)            
        if numero_planeta==9:
            x=realiza_verlet(posiciones_anteriores_x[9],posiciones_x[9],ax)
            y=realiza_verlet(posiciones_anteriores_y[9],posiciones_y[9],ay)
            pos_plutonx.append(x)
            pos_plutony.append(y)
            
           
    return pos_mercuriox,pos_mercurioy,pos_venusx,pos_venusy,pos_tierrax,pos_tierray,pos_martex,pos_martey,pos_jupiterx,pos_jupitery,pos_saturnox,pos_saturnoy,pos_neptunox,pos_neptunoy,pos_plutonx,pos_plutony
    

def main():
    diax=[0]
    dia=1
    print("inserte dias totales")
    dias=int(input())
    while dia<dias-1:
            posiciones_todas=ciclo(dia)
            dia=dia+1
            diax.append(dia)
    plt.show()

    plt.plot(pos_tierrax,pos_tierray,"blue")
    plt.plot(pos_mercuriox,pos_mercurioy,"red","- -")
    plt.plot(pos_venusx,pos_venusy,"green")
    plt.plot(pos_martex,pos_martey,"orange")
   # plt.plot(pos_jupiterx,pos_jupitery,"yellow")
   # plt.plot(pos_saturnox,pos_saturnoy,"grey")
   # plt.plot(pos_neptunox,pos_neptunoy,"pink")
   # plt.plot(pos_uranox,pos_uranoy,"brown")
    
    plt.plot(0,0,"yo")
    plt.show()
    



        