#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:57:38 2020

@author: droliver
"""

import numpy as np
import pandas as pd
from math import ceil


populacao = 150
amostra = 15
divisao = ceil(populacao/amostra)

#sorteio
randomic = np.random.randint(low = 1, high = divisao + 1, size = 1)

acumulador = randomic[0]

sorteados = []

for i in range(amostra):
    sorteados.append(acumulador += divisao)
    
sorteados