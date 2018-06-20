#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 14:23:04 2017

@author: jean mario moreira de lima
"""

import numpy as np
import matplotlib.pyplot as plt

#ANN in python

def fresadora(t):
    return ((2/5) + (1/10 * np.e**(-5*t)) - ((1/2) * np.e**(-t)))

def funcSigmoide(x):
    return (2/(1 + np.exp(-2*x))) - 1

def dFuncSigmoide(x):
    return (1 - (((2/(1 + np.exp(-2*x))) - 1)**2))

def runBackpropagation(funAtiva, adjustFactor, maxEpoch, maxError, entradasX, targetsY, w1, w2):
    for epoch in range(maxEpoch):
        nAmostras = len(entradasX)
        E = np.zeros((len(nAmostras))
        for k in range(nAmostras):
          print(k)
          x1 = entradasX[k];
          tY = targetsY[k];
          """1. Propagação """ 
          """1.1 Camada Oculta """
          """1.1.1 Potencial de ativação de cada neuronio"""
          uN1 = w1[0,0]*1 + w1[0,1]*x1
          uN2 = w1[1,0]*1 + w1[1,1]*x1
          uN3 = w1[2,0]*1 + w1[2,1]*x1
          
          """1.1.2 Sinal de Saída do Neurônio"""
          yN1 = funAtiva(uN1)
          yN2 = funAtiva(uN2)
          yN3 = funAtiva(uN3)
          
          """1.2 Camada de Saida """
          """1.2.1 Potencial de Ativação """
          uNs = w2[0,0]*1 + w2[0,1]*yN1 + w2[0,2]*yN2 + w2[0,3]*yN3
          
          """1.2.2 Saída do Neuronio - Ativação Linear"""
          y = uNs
          
          """2. Retropropagação"""
          """ erro de trein - camada de saída """
          e = tY - y
          E[k] = e
          
          """Ajuste dos pesos da camada de saída"""
          """--Gradiente local da camada 2 (saída)--"""
          """--- grad2 = e * dF(linear) = e * 1 = e --- """
          gradCamada2 = e;
          
          """fator de ajuste dos pesos"""
          dw2[0,0] = adjustFactor * gradCamada2 #bias
          dw2[0,1] = adjustFactor * gradCamada2 * yN1
          dw2[0,2] = adjustFactor * gradCamada2 * yN2
          dw2[0,3] = adjustFactor * gradCamada2 * yN3
          
          """ajuste dos pesos"""
          w2[0,0] = w2[0,0] + dw2[0,0]
          w2[0,1] = w2[0,1] + dw2[0,1]
          w2[0,2] = w2[0,2] + dw2[0,2]
          w2[0,3] = w2[0,3] + dw2[0,3]
          
          """Ajuste de pesos da camada oculta """
          """ Gradiente Local da Camada oculta 1 """
          sumGrad1 = gradCamada2 * (w2[0,1] + w2[0,2] + w2[0,3])
          
          """Neuronio 2 da camada oculta"""
          
          grad1N1 = sumGrad1 * dFuncSigmoide(uN1)
          
          """Neuronio 2 da camada oculta"""
          grad1N2 = sumGrad1 * dFuncSigmoide(uN2)
          
          """Neuronio 2 da camada oculta"""
          grad1N3 = sumGrad1 * dFuncSigmoide(uN3)
          
          """fator de ajuste dos pesos"""
          """Neuronio 1 da camada oculta"""
          dw1[0,0] = adjustFactor * grad1N1
          dw1[0,1] = adjustFactor * grad1N1 * x1
          
          """Neuronio 2 da camada oculta"""
          dw1[1,0] = adjustFactor * grad1N2
          dw1[1,1] = adjustFactor * grad1N2 * x1
          
          """Neuronio 3 da camada oculta"""
          dw1[2,0] = adjustFactor * grad1N3
          dw1[2,1] = adjustFactor * grad1N3 * x1
          
          """Ajuste dos pesos """
          """ Neuronio 1 da camada oculta"""
          w1[0,0] = w1[0,0] + dw1[0,0] #bias
          w1[0,1] = w1[0,1] + dw1[0,1] #n1
          
          """Neuronio 2 da camada oculta"""
          w1[1,0] = w1[1,0] + dw1[1,0] #bias
          w1[1,1] = w1[1,1] + dw1[1,1] #n2
          
          """Neuronio 3 da camada oculta"""
          w1[2,0] = w1[2,0] + dw1[2,0] #bias
          w1[2,1] = w1[2,1] + dw1[2,1] #n3
          
      Em = (np.matrix(E) * np.matrix(E).transpose())/2
          
          
          
          
          
    
          
          
          
    

#float range frange
entradasX = np.arange(0,10,0.25)
targetsY = fresadora(entradasX)

print("\nEntradas e Saídas\n")

plt.figure(1),
plt.subplot(211),plt.plot(entradasX,'red'), plt.grid()
plt.subplot(212),plt.plot(targetsY,'blue'),plt.grid()
plt.savefig('plot1.eps')

#networks parameters

nAmostras = len(entradasX);
maxEpoch = 1000
maxError = 10 ** -10
adjustFactor = 0.005
