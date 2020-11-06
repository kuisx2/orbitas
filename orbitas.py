# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 14:48:23 2020

@author: facun
"""
import matplotlib.pyplot as plt
import random
import numpy as np
import imageio


def calcular_delta(x_sol,x_tierra):
    delta=(x_sol-x_tierra)
    return delta

def dis_trigo(pos_sol,pos_tierra):
    x=calcular_delta(pos_sol[0],pos_tierra[0])
    y=calcular_delta(pos_sol[1],pos_tierra[1])
    distancia= np.sqrt(x**2+y**2)
    return distancia

def calcula_aceleracion ( pos_sol , pos_tierra ) :    
    d=dis_trigo(pos_sol,pos_tierra)
    dx=calcular_delta(pos_sol[0],pos_tierra[0])
    dy=calcular_delta(pos_sol[1],pos_tierra[1])
    a=(G*M)/(d**2)
    ax=a*(dx)/d
    ay=a*(dy)/d
    a=[ax,ay]
    return a

def realiza_verlet(pos_anterior,pos_actual,aceleracion_actual,dt):

    x=2*pos_actual[0]-pos_anterior[0]+aceleracion_actual[0]*(dt**2)
    y=2*pos_actual[1]-pos_anterior[1]+aceleracion_actual[1]*(dt**2)
    return [x,y]

def paso_dias(lista_x,lista_y,tiempo_total,dias,dt):
    pos_sol=[0,0]
    lista_aceleracion_y=[]
    lista_aceleracion_x=[]
    for i in range (1 , tiempo_total-1,1 ) :
# Genero listas con las posiciones
        pos_actual =[ lista_x[i],lista_y[i]]
        pos_anterior=[lista_x[i-1],lista_y[i-1]]
# Calculo la aceleracion
        aceleracion=calcula_aceleracion( pos_sol , pos_actual )
# Calculo la posicion futura
        pos_posterior=realiza_verlet(pos_anterior,pos_actual,aceleracion,dt)
# Guardo las ultimas posiciones
        lista_x.append (pos_posterior[0])
        lista_y.append (pos_posterior[1])
# Guardo las ultimas aceleraciones
        lista_aceleracion_x.append (aceleracion[0] )
        lista_aceleracion_y.append (aceleracion[1] )
# Guardo el dia
        dias.append ( i+1 )
    
    return lista_x,lista_y,lista_aceleracion_x,lista_aceleracion_y,dias

def hacer_foto ( lista_x , lista_y , pos_sol , dia) :
# borra lo que hubiera antes en la figura
    plt . clf ()
# grafico trayectoria (x,y)
    plt . plot ( lista_x,lista_y ,"g")
# grafico al Sol
#’yo ’ es para hacer un punto amarillo ( ’y’ de yellow y ’o’ de punto )
#ms elige el tamanio del punto
    plt . plot (pos_sol[0],pos_sol[1] ,"yo", ms =20)
# grafico a la Tierra mas chiquita
#’b’ es por blue
    plt . plot (lista_x[dia],lista_y[dia], "bo" , ms =10)
    
#    plt.arrow(lista_x[dia], lista_y[dia] , lista_aceleracion_x[dia]*10**12.5, lista_aceleracion_y[dia]*10**12.5,width=10**9.5,Color="g")

    return 

def hacer_video ( lista_x , lista_y , pos_sol , nombre_video ) :
    lista_fotos =[] # aca voy a ir guardando las fotos
    for i in range (len ( lista_x ) ) :
        if i %4==0: # esto es para guardar 1 de cada 2 fotos y tarde menos
            hacer_foto ( lista_x , lista_y, pos_sol , i )
            plt.savefig ( nombre_video +".png")
            lista_fotos . append ( imageio . imread ( nombre_video +".png") )
            #print (str( i ) + "de" + str(len( lista_x ) ) +" fotos guardadas ")
            imageio . mimsave ( nombre_video +".mp4", lista_fotos ) # funcion que crea el video
    return print ("Video Guardado ")

#def funcion_vel(lista_x,lista_y,lista_aceleracion_x,lista_aceleracion_y,dia,dt):
#    velx=[0]
 #   vely=[0]
 #   for i in range(1,dia,1):
  #      velx.append=velx[i-1]+2*lista_aceleracion_x*dt
   #     vely.append=vely[i-1]+2*lista_aceleracion_y*dt
    #return velx,vely
    
# =============================================================================
# tierra
# =============================================================================
dias = [0,1]
pos_sol = [0 ,0] # (x,y) del Sol
UA=149597871.0
G = 6.693*(10**-11) # Constante de gravitacion en notacion cientifica 
M = 1.98*(10**30)
lista_x = [147095000000.0, 147095000000.0]
lista_y = [0.0, 2617920000.0]
dt=60 * 60 * 24
tiempo_total=400
lista_aceleracion_x =[]
lista_aceleracion_y =[]
pos_tierra = [lista_x[0],lista_y[0]]
aceleraciones = calcula_aceleracion ( pos_sol , pos_tierra )
lista_aceleracion_x.append (aceleraciones[0])
lista_aceleracion_y.append (aceleraciones[1])
pos_tierra1 = [lista_x[1],lista_y[1]]
aceleraciones = calcula_aceleracion ( pos_sol , pos_tierra1 )
lista_aceleracion_x.append (aceleraciones[0])
lista_aceleracion_y.append (aceleraciones[1])

siguiente=paso_dias(lista_x,lista_y,tiempo_total,dias,dt)
lista_aceleracion_x.append (siguiente[2])
lista_aceleracion_y.append (siguiente[3])
# =============================================================================
# marte
# =============================================================================
#lista_xm = [-147095000000.0, -147095000000.0]
#lista_ym = [0.0, 2617920000.0]
#dias = [0,1]
#dt=60 * 60 * 24
#tiempo_total=0
#tiempo_total=400
#lista_aceleracion_xm =[]
#lista_aceleracion_ym =[]
#pos_marte = [lista_xm[0],lista_ym[0]]
#aceleracionesm = calcula_aceleracion ( pos_sol , pos_marte )
#lista_aceleracion_xm.append (aceleracionesm[0])
#lista_aceleracion_ym.append (aceleracionesm[1])
#pos_marte1 = [lista_xm[1],lista_ym[1]]
#aceleracionesm = calcula_aceleracion ( pos_sol , pos_marte )
#lista_aceleracion_xm.append (aceleracionesm[0])
#lista_aceleracion_ym.append (aceleracionesm[1])
#siguientem=paso_dias(lista_xm,lista_ym,tiempo_total,dias,dt)
#lista_aceleracion_xm.append (siguientem[2])
#lista_aceleracion_ym.append (siguientem[3])




# =============================================================================
# representacion
# =============================================================================
v0=lista_x
v1=lista_y

plt . figure ()

plt.plot(dias,lista_x,"r",)
plt.plot(dias,lista_y,"b",)


plt.show()


#vel=funcion_vel(lista_x,lista_y,lista_aceleracion_x,lista_aceleracion_y,200,dt)





video=hacer_video ( lista_x , lista_y , pos_sol , "video" )

