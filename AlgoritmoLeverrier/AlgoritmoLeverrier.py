# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:08:57 2015


@author: jeanmarioml
"""
import pylab as pl;
import numpy as np;
import scipy as sp;

A = [[-1, 0, 0],[0,0,-1],[0,1,-1]];


def leverrier(A):
    
    #ordem
    n = len(A);
    
    #array de alphas -(tracos)/n necessario para o calculo do delta(s)
    alphas = np.arange(n+1);
    #o array alphas para n = 0 sempre sera 1
    alphas[0] = 1;
    
    #definindo A como uma matriz numpy para utilizacao dos recursos da biblioteca
    A_ = np.mat(A);
    
    #definindo as matrizes R com valor inicial de 0 ate n*n*n - 1;
    R = np.arange(n*n*n).reshape(n,n,n)
    for i in range(n):
        if(i == 0):
            for j in range(n):
                for k in range(n):
                    if (j == k):
                        R[i][j][k] = 1;
                    else:
                        R[i][j][k] = 0;
        else:
            #matriz temporaria que e o resultado na multiplicacao entre as matrizez A e R[n-1]
            mat_temp = A_ * R[i-1];
            #utiliza a funcao traco para calculo do alpha
            alpha = -1 * (traco(mat_temp)/float(i));
            alphas[i] = alpha;
            #atribui valores a R, sendo Rn = ARn-1 + alpha * I sendo I a matriz identidade
            #que eh igual a R[0]
            R[i] = mat_temp + (alpha * R[0]);
            if(i == n-1):
                alphas[i+1] = -1 * (traco((A_ * R[i]))/float(i+1));
    
    #Calculo de delta(S):
    print alphas;
    delta_s = "1 / ";
    
    for i in range(n+1):
        if(i != 3):
            delta_s = delta_s + "s_" + str(n-i) + "*" + str(alphas[i]) + " + ";
        else:
            delta_s = delta_s + "s_" + str(n-i) + "*" + str(alphas[i]) + "  ";
        
    #Calculo da adjunta
         
    #Variaveis auxiliares para exibir a matriz adjunta
    adjunta = "";
    aux = 0;
        
    for i in range(n):
        for j in range(n):
            for k in range (n):  
                if(R[k][i][j] != 0):
                    if(k != 2):
                        adjunta = adjunta + "s_"+str(n-1-k)+"*"+str(R[k][i][j])+"+";
                    else:
                        adjunta = adjunta + "s_"+str(n-1-k)+"*"+str(R[k][i][j])+"    "; 
                else:
                    aux = aux + 1;
                    if (aux == 3):
                        adjunta = adjunta + str(R[k][i][j])+"    "+ " ";
                        aux = 0;
        if(i == 0):
            adjunta = adjunta + "|" + delta_s;
        else:
            adjunta = adjunta + "|";
        print adjunta;
        adjunta = " ";
    return A; 


    
    
#retorna o traco da matriz
def traco(A):
    soma = 0;
    
    for i in range(len(A)):
        for j in range (len(A)):
            if (i == j):
                soma = soma + A[i,j];
            
    return soma;

def printNome():
    print "nome";
return echo -p "deu certo";
