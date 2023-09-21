# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 14:18:56 2023

@author: RYZEN
"""

import time
import numpy as np

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm
from matplotlib import colors
plt.style.use('dark_background')

from matplotlib import rc
rc("animation", html = "jshtml")

dx = 0.02   
L = 1.0
t_max = 1.5

# condiciones de frontera 
l0 = 0
lL = 0
a = 1
A = (30/(a**5))**(1/2)
Ni = [1,2,3,4,5]


# condiciones iniciales
def onda(x, n):
    return A*x*(a-x)*np.sin(n*np.pi * x/a)

def vel_ini(x):
    return np.zeros(len(x))

def solucion_ecuacion_onda_1D(dx,t_max,L,l0,lL, n):
    dt = dx
    r = (dt/dx)**2
    a = 2*(1-r)
    x = np.linspace(0, L, num = 1+int(np.round((L)/dx)))
    lt = 1+int(np.round((t_max)/dt))
    lx = len(x)
    U = np.zeros([lt,lx])
    U[0,:] = onda(x, n)
    v0 = vel_ini(x)
    U[:,0] = l0
    U[:, -1] = lL
    for i in range(1,lx-1):
      U[1,i] = 0.5*a*U[0,i] + 0.5*r*(U[0,i-1] + U[0,i+1]) + dt*v0[i]
    
    for n in range(1,lt-1): # time
      for i in range(1,lx-1): # space
        U[n+1,i] = a*U[n,i] + r*(U[n,i-1] + U[n,i+1]) - U[n-1,i]
    return x, U

def update(num_frame, U, line):
    line.set_ydata(U[num_frame,:])  # update the data.
    return line,

def crear_animacion(x, U, name):
    N = U.shape[0]
    fig = plt.figure(figsize = (9,5), dpi=75)
    ax = plt.gca()
    ax.set_xlim([0,L])
    ax.set_ylim([np.min(U)-1,np.max(U)+1])
    
    line, = ax.plot(x,U[0],'r')
    plt.tight_layout()
    ani = animation.FuncAnimation(fig, update, N, fargs=(U,line))
    return ani
    #ani.save(name,fps=30)
    #plt.close(fig)


"NIVEL DE ENERGIA 1"
start_time = time.time()
x, U = solucion_ecuacion_onda_1D(dx,t_max,L,l0,lL, 1)
print("Tiempo usado en calcular la solución(s):",time.time() - start_time)

print('x.shape:',x.shape, ' U.shape:', U.shape)


start_time = time.time()
crear_animacion(x, U, "ecuacion_onda_1D_estado_1.gif")
#print("Tiempo usado en crear la animación (s):",time.time() - start_time)

"NIVEL DE ENERGIA 2"
start_time = time.time()
x, U = solucion_ecuacion_onda_1D(dx,t_max,L,l0,lL, 2)
print("Tiempo usado en calcular la solución(s):",time.time() - start_time)

print('x.shape:',x.shape, ' U.shape:', U.shape)


start_time = time.time()
crear_animacion(x, U, "ecuacion_onda_1D_estado_2.gif")
#print("Tiempo usado en crear la animación (s):",time.time() - start_time)

"NIVEL DE ENERGIA 3"
start_time = time.time()
x, U = solucion_ecuacion_onda_1D(dx,t_max,L,l0,lL, 3)
print("Tiempo usado en calcular la solución(s):",time.time() - start_time)

print('x.shape:',x.shape, ' U.shape:', U.shape)


start_time = time.time()
crear_animacion(x, U, "ecuacion_onda_1D_estado_3.gif")
#print("Tiempo usado en crear la animación (s):",time.time() - start_time)

"NIVEL DE ENERGIA 4"
start_time = time.time()
x, U = solucion_ecuacion_onda_1D(dx,t_max,L,l0,lL, 4)
print("Tiempo usado en calcular la solución(s):",time.time() - start_time)

print('x.shape:',x.shape, ' U.shape:', U.shape)


start_time = time.time()
crear_animacion(x, U, "ecuacion_onda_1D_estado_4.gif")
#print("Tiempo usado en crear la animación (s):",time.time() - start_time)

"NIVEL DE ENERGIA 5"
start_time = time.time()
x, U = solucion_ecuacion_onda_1D(dx,t_max,L,l0,lL, 5)
print("Tiempo usado en calcular la solución(s):",time.time() - start_time)

print('x.shape:',x.shape, ' U.shape:', U.shape)


start_time = time.time()
crear_animacion(x, U, "ecuacion_onda_1D_estado_5.gif")
#print("Tiempo usado en crear la animación (s):",time.time() - start_time)