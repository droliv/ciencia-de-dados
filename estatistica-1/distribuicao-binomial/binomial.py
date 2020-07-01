# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:54:08 2020

@author: reis-
"""


from scipy.stats import binom

#jogar uma moeda 5 vezes e dar cara 3 vezes
x = 3 #sucessos
n = 5 #tentativas
p = 0.5 #probabilidade


print(binom.pmf(x, n, p))

#passar por 4 sinais de 4 tempos e pegar (0,1,2,3,4) sinais verdes

# 0 sinais verdes
print(binom.pmf(0, 4, 0.25))

# 1 sinal verde
print(binom.pmf(1, 4, 0.25))

#2 sinais verdes
print(binom.pmf(2, 4, 0.25))

#3 sinais verdes
print(binom.pmf(3, 4, 0.25))

#4 sinais verdes
print(binom.pmf(4, 4, 0.25))

#acertar 7 questões em uma prova com 12 questões chutando as alternativas.

print(binom.pmf(7, 12, 0.25))






