#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:32:53 2019

@author: jeanmarioml
"""

#Python Relampago

5 / 2 #divisão
5 // 2 #divisao por inteiro

#1.Funções

def double(x):
    return 2*x

double(2)

#1.1 Função são PRIMEIRA CLASSE -> atribuir a variaevis ou passar a outras funções

def aplicar_a_um(f):
    return f(1)

dobro = double
x = aplicar_a_um(dobro)

#1.2 Existe as pequenas funções ou LAMBDAS
y = aplicar_a_um(lambda x: x+4)

#1.3 Parâmetros podem receber argumentos padrão

def meu_print(message="minha mensagem padrao"): 
    print (message)
        
meu_print("Ola Mundo!")
meu_print()

#1.4 Especificando argumento pelo nome

def adicao(a=0,b=0):
    return a+b

print (adicao(10,5))
print (adicao(0,5))
adicao(b=10)

##### STRINGS #####

#1. Podem ser determinadas por ASPAS SIMPLES ou DUPLAS.

