#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 14:29:16 2020

@author: droliver
"""

import pandas as pd
from sklearn.model_selection import train_test_split

iris = pd.read_csv('iris.csv')

#contagem de itens pela coluna class
iris['class'].value_counts()

#amostra de acordo com a quantidade de registros da coluna com a mesma proporçao

x, _, y, _ = train_test_split(iris.iloc[:, 0:4], iris.iloc[:, 4], test_size = 0.5,
                              stratify = iris.iloc[:, 4])

y.value_counts()


#amostra estratificada com proporçoes diferentes
infert = pd.read_csv('infert.csv')
infert['education'].value_counts()
#0 a 5 - 12   -- 12/248*100 = 5
#6 a 11 - 120 -- 120/248*100 = 48
#12+ - 116    -- 116/248*100 = 47

x, _, y, _ = train_test_split(infert.iloc[:, 2:9], infert.iloc[:, 1], test_size = 0.6,
                              stratify = infert.iloc[:, 1])  
y.value_counts()

