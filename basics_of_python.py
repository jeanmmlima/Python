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

string_aspas_simples = 'data science'
string_aspas_duplas = "data science"

#1.1 python usa barra invertida para codificar caracteres especiais

tab = "\t"
no_tab = r"\t"

#1.2 String com múltiplas linhas

multi_linhas = """primeira linha.
segunda linha.
terceir linha."""

##### EXCEÇÕES #####

#1. Manipulando exceçõe com TRY e EXCEPT

try:
    print(0/0)
except ZeroDivisionError:
    print ("Divisão por zero não é possível")


##### LISTAS #######
    
#list ->  ED mais básica do python. Coleção ordenada de dados.

lista_inteira = [1, 2, 3]    
lista_mix = ["texto", 0.1, False]
lista_de_listas = [lista_inteira, lista_mix, []]

soma_lista = sum(lista_inteira)
tam_lista = len(lista_mix)

#1. colchetes [ ] configura o n-ésimo elemento de uma lista

x = list(range(10))# 0, 1 ... 9 Python 3.x deve converter elementos do range para list

zero = x[0]
x[0] = -1
nove = x[-1] #retorna 9, Pythonic para ultimo elemento
oito = x[-2] #retorna 8, Pythonic para penultimo elemento

#2. colchetes [ ] para repartir listas

primeiros_tres = x[:3]
um_2_quatro = x[1:5]
ultimos_tres = x[-3:]

#3. Operador IN para verificar associação a lista

1 in [1, 2, 3] #true

#4. Concatenação de Listas e Adição de Dados

x = [1, 2, 3]
x.extend([4, 5, 6])

y = x + [7, 8, 9]

x.append(0) #adicional elemento ao final dalista

y = x[-1]

#mesmo numero de elmentos dos dois lados
x, y = [[1,2], [2,3]] #atribui valores da lista a variaveis.

_,y = [1,2] #y = 2 e 1 é descartado

##### TUPLAS ######

#Tuplas são similares as listas, entretanto NÃO PODEM SER MODIFICADAS

lista = [1, 2, 3]
tupla = (1, 2, 3)
tupla2 = 4, 5, 6

lista[2] = 5

try:
    tupla[1] = 5
except TypeError:
    print ("Tupla não pode ser modifcada")    

#1. maneira eficaz de retornar múltiplos valores a partir das funções
    
def soma_e_prod(x,y):
    return (x+y),(x*y)

sp = soma_e_prod(2,3)
s,p = soma_e_prod(5,10)

##### DICIONARIOS ######