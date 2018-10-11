# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 19:49:33 2018

@author: Thiagarajan
"""

import pandas as pd
import numpy as np

#dataset = pd.read_csv('bitstamp.csv')
# df DataFrame for pandas. Need to convert data in to pandas dataframe
#print (dataset.describe())
#df = pd.DataFrame(dataset)
#print(df.head(10))

arr = np.arange(1,26).reshape(5,5)
print(arr)
print(arr[2:4,1:3])
ar = np.ones(10)
ar = ar + 10
print(ar)