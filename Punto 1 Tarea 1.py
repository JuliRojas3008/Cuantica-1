# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt


X = np.linspace(100,3000, 3000)
T = [10000, 8000, 5000, 3000]
h = 6.62607015 *(10**-34)
c = 3*(10**8)
k = 1.380649 * (10**-23)

#PARTE A
def funcion (x, t):
    Y = ((8*np.pi*h)/((x/(10**9))**3))*(1/(np.exp((h*c)/((x/(10**9))*k*t))-1))
    return Y

def graficar(x,T):
    for t in T:
        Y = funcion(x,t)
        plt.plot(X,Y, label=str(t)+ " K")
    plt.xlabel("Longitud de Onda λ (nm)", size = 10,)
    plt.ylabel("Densidad de energía/frecuencia u¸(T) (µJ/m^3/GHz)", size = 10)
    plt.title("Radiación De Cuerpo Negro", 
              fontdict={'family': 'serif', 
                        'color' : 'darkblue',
                        'weight': 'bold',
                        'size': 18})
    
    plt.grid(True)
    plt.legend()
    #plt.figure(figsize=(10,6))
    plt.show()



#PARTE B
def calcular(x,T):
    longmas=[]
    for t in T:
        Y = funcion(x,t)
        mayor = 0
        longma = 0
        for i in range(len(x)):
            if Y[i]> mayor:
                mayor = Y[i]
                longma = x[i]
        longmas += [longma]
    return longmas

def imprimir_valores(X,T):
    long = calcular(X,T)
    for i in range(len(T)):
        print("La longitud con maxima intensidad para " + str(T[i])+ " K es de " + str(long[i]) +" nm")



#PARTE C

T1 = 10000
S = np.linspace(0,1200, 1000)
def funcionc (s):
    Y = ((8*np.pi*((s*(10**12))**2))/(c**3))*((h*(s*(10**12)))/(np.exp((h*(s*(10**12)))/(k*T1))-1))
    return Y

def funcionc_Rayleigh_Jeans(s):
    Y = ((8*np.pi*((s*(10**12))**2))/((c)**3))*k*T1
    return Y

def graficarc(s):
    YC = funcionc(s)
    YCR = funcionc_Rayleigh_Jeans(s)
    plt.plot(S,YC, label="Planck")
    plt.plot(S,YCR, label="Rayleigh-Jeans")
    plt.xlabel("Frecueancia de Onda λ (Hz)", size = 10,)
    plt.ylabel("Densidad de energía/frecuencia u¸(T) (µJ/m^3/GHz)", size = 10)
    plt.title("Radiación De Cuerpo Negro para 10000 K", 
              fontdict={'family': 'serif', 
                        'color' : 'darkblue',
                        'weight': 'bold',
                        'size': 18})
    plt.grid(True)
    plt.legend()
    plt.ylim(0,8.6e-15)
    plt.show()



def mostrar_menu_aplicacion() -> bool:
    print("Menu de opciones")
    print(" 1 - Graficar el punta A")
    print(" 2 - Calcular el punto B")
    print(" 3 - Graficar el punto C")
    print(" 4 - Salir de la aplicacion.")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        graficar(X,T)
    elif opcion_elegida == "2":
        imprimir_valores(X, T)
    elif opcion_elegida == "3":
        graficarc(S)
    elif opcion_elegida == "4":
        print("Gracias por su atencion, espero el punto 1 de la tarea 1 haya sido de tu agrado.\n")
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    return continuar_ejecutando

def iniciar_aplicacion():
    
    print("Bienvenid@ a nuestro punto 1 de la tarea 1 de mecánica cuántica!!!!\n")
    print("Para los puntos A y B se manejará la siguiente lista de temperaturas \n")
    print(T)
    print("\n")
    print("Para el punto C manejaremos una tempreaturaa de 10000 K\n")
    print("Recordar que las escalas de las gráficas se encuentran al final de cada eje")
    ejecutando = True
    while ejecutando:
        ejecutando = mostrar_menu_aplicacion()

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")
            
            
iniciar_aplicacion()
    
