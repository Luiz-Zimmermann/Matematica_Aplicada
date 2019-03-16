# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:06:02 2019

@author: Luiz Zimmermann
"""
import numpy as np
import matplotlib.pyplot as pl 
import scipy 
from scipy import signal


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
t = np.arange(-1, 4, 1)
 
for x in t:
   n = signal.unit_impulse(6,t[x])
   print(n, x)
    
    
 
    
 
