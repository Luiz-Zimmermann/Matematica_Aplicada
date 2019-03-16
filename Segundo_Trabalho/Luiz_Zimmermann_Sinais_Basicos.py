# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:54:33 2019

@author: Luiz Zimmermann
"""


import numpy as np
import matplotlib.pyplot as pl

#Criando um vetor com valores que serão usados em todos os graficos
t = np.arange(-5,5,0.01)
t60 = np.arange(0,0.1,0.001)

#Calculos dos exemplos das funções exponeciais reais
x = 3*(np.exp(2*t))
y = 3*(np.exp(-2*t))

#Calculos dos exemplos das funções exponeciais Complexas
x1 = 3*(np.exp(1j*(2*t)))

#Calculos dos exemplos das funções cossenoidais
x2 = 220 * np.sqrt(2) * np.sin(2 * np.pi * 60 * t60)
 

#Nome da figura e tamanho da janela a ser aberta
pl.figure(u'Sinais Basicos',figsize=(10, 6))

#Plota os graficos reais
pl.subplot(2,2,1)
pl.title('3e^2t')
pl.grid(True)
pl.xlabel('t')
pl.plot(t, x)

pl.subplot(2,2,2)
pl.title('3e^-2t')
pl.grid(True)
pl.xlabel('t')
pl.plot(t, y)

#Plota os graficos complexos
pl.subplot(2,2,3)
pl.title('3e^j2t')
pl.grid(True)
pl.xlabel('t')
pl.plot(t,x1)

#Plota os graficos cossenoidais 
pl.subplot(2,2,4)
pl.title(r'220$\sqrt{2}\sin(2\pi$60t)')
pl.grid(True)
pl.xlabel('t')
pl.plot(t60, x2)


 
pl.tight_layout()
pl.show()