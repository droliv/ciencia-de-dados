#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:28:52 2020

@author: droliver
"""
import numpy as np
from scipy import stats

salarios_jogadores = [40000, 18000, 12000, 250000, 30000, 140000, 300000, 40000, 800000]

#media
np.mean(salarios_jogadores)

#mediana
np.median(salarios_jogadores)

#quartis
quartis = np.quantile(salarios_jogadores, [0, 0.25, 0.5, 0.75, 1])
quartis

#desvio padrao
np.std(salarios_jogadores, ddof = 1)

# resumo dos dados
stats.describe(salarios_jogadores)
