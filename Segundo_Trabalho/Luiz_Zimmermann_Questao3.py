# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 17:01:39 2019

@author: Luiz Zimmermann
"""
import numpy as np
import matplotlib.pyplot as pl 

#função para simular o degrau unitário
def u(t):
    z = []
    for x in t:
        if x >= 0.0:
            z.append(1)
        else:
            z.append(0)
    return z

 
#vetor com valores de t para realizar os exemplos
t = np.arange(-4, 4.1 , 0.1)
 
#função f(t), inicia em -2, sobe ate 2 em t=-1, e inicia a exponencial em t=1
z1 = (((2 * (t+2) * u(t+2)) - (2*(t+1) * u(t+1)))
            -(((2 * (t+2) * u(t+2)) - (2*(t+1) * u(t+1)))*u(t-1))) + ((2 * np.e ** -(t - 1)) * u(t - 1))
#função f(-t) a exponencial começa em t=-4 e acaba em t=-1, depois a função continua de t=-1 ate t=1, onde começa a decrescer,até t=2
z2 = (((2 * (-t+2) * u(-t+2)) - (2*(-t+1) * u(-t+1)))
            -(((2 * (-t+2) * u(-t+2)) - (2*(-t+1) * u(-t+1)))*u(-t-1))) + ((2 * np.e ** -(-t - 1)) * u(-t - 1))
            
#Cálculo para achar a parte par da função
par = 1/2*(z1+z2)
#Cálculo para achar a parte impar da função
impar = 1/2*(z1-z2)

#Nome da figura e tamanho da janela a ser aberta
pl.figure(u'Questão 3',figsize=(10, 6))

#função f(t)
pl.subplot(221)
pl.title('f(t)')
pl.plot(t,z1)
pl.grid(True)

#função f(-t)
pl.subplot(222)
pl.title('f(-t)')
pl.plot(t,z2)
pl.grid(True)

#parte par de f(t)
pl.subplot(223)
pl.title('Par')
pl.plot(t,par)
pl.grid(True)

#parte impar de f(t)
pl.subplot(224)
pl.title('Impar')
pl.plot(t,impar)
pl.grid(True)

 

pl.tight_layout()
pl.show()



