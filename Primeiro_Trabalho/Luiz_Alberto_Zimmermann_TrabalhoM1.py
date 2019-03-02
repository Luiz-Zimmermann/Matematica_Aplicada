# -*- coding: utf-8 -*-
#Programa feito por Luiz Alberto Zimmermann

import numpy as np
import matplotlib.pyplot as pl

#Vetor usado para armazenar os valores de omega(W) utilizados para criar o grafico
vetorW = np.arange(-5, 5, 0.1)

#Calculo da questao 4 alternativa a)

z1 = (3)/(3 + (1j*vetorW))

#--------------------------

#Calculo da questao 4 alternativa b)

z2 = 5 * (1j*vetorW) / (3 + 1j*vetorW)

#--------------------------

#Nome da figura e tamanho da janela a ser aberta
pl.figure(u'Gráficos questão 4',figsize=(8, 6))

#Desenha os graficos da questao 4 a)
#Magnitude em função de omega(W)
pl.subplot(2, 2, 1)
pl.title(u'Magnitude(4a)') 
pl.grid(True)
pl.ylabel("|Z1($\omega$)|")
pl.xlabel("$\omega$", labelpad=-1)
pl.xticks(np.arange(-5, 5, 1))
pl.yticks(np.arange(0, 2, 0.1))
pl.plot(vetorW, abs(z1))

#Fase em função de omega(W)
pl.subplot(2, 2, 2)
pl.title(u'Fase(4a)') 
pl.grid(True)
pl.ylabel(r"$\theta1(\omega$)", labelpad=-7)
pl.xlabel("$\omega$", labelpad=-1)
pl.xticks(np.arange(-5, 5, 1))
pl.yticks(np.arange(-60,80, 20))
pl.plot(vetorW, np.degrees(np.arctan(z1.imag/z1.real)))

#------------------------------------------------------

#Desenha os graficos da questao 4 b)
#Magnitude em função de omega(W)
pl.subplot(2, 2, 3)
pl.title(u'Magnitude(4b)') 
pl.grid(True)
pl.ylabel("|Z2($\omega$)|")
pl.xlabel("$\omega$", labelpad=-1)
pl.xticks(np.arange(-5, 5, 1))
pl.yticks(np.arange(0, 5, 1))
pl.plot(vetorW,abs(z2))

#Fase em função de omega(W)
pl.subplot(2, 2, 4)
pl.title(u'Fase(4b)') 
pl.grid(True)
pl.ylabel(r"$\theta2(\omega$)",labelpad=-7)
pl.xlabel("$\omega$", labelpad=-1)
pl.xticks(np.arange(-5, 5, 1))
pl.yticks(np.arange(-80,90, 20))
pl.plot(vetorW, np.degrees(np.arctan(z2.imag/z2.real)))

#------------------------------------------------------

pl.tight_layout()
pl.show()
