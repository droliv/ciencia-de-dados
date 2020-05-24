#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:14:14 2020

@author: droliver
"""
#importar o pandas e numpy
import pandas as pd
import numpy as np


base = pd.read_csv('iris.csv')

# seed pode ser usado para repetir sempre a mesma amostra ao executar
np.random.seed(2345)
# criar uma amostra aleatoria contendo 0 e 1 com a mesma probabilidade.
amostra = np.random.choice(a = [0,1], size=150, replace=True, p = [0.5,0.5])

#tamanho da amostra
len(amostra)

#quantidade de 1 na amostra
len(amostra[amostra == 1])

#quantidade de 0 na amostra
len(amostra[amostra == 0])
