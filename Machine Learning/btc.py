# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 19:27:15 2018

@author: Thiagarajan
"""

#Importing preprocessing libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


training_set=pd.read_csv('bitstamp.csv')      #reading csv file

training_set1=training_set.iloc[:,1:2]        #selecting the second column
print (training_set1.head())                  #print first five rows
training_set1
training_set1=training_set1.values            #converting to 2d array
training_set1                                 #print the whole data


#Scaling the data

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler()                           #scaling using normalisation 
training_set1 = sc.fit_transform(training_set1)
xtrain=training_set1[0:2148]                  #input values of rows [0-2149]		   
ytrain=training_set1[11:2159]                  #input values of rows [1-2150]

today=pd.DataFrame(xtrain[0:5])               #assigning the values of xtrain to today
tomorrow=pd.DataFrame(ytrain[0:5])            #assigning the values of ytrain to tomorrow
ex= pd.concat([today,tomorrow],axis=1)        #concat two columns 
ex.columns=(['today','tomorrow'])
print(ex)
xtrain = np.reshape(xtrain, (2148, 1, 1))     #Reshaping into required shape for Keras

#importing keras and its packages

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM


regressor=Sequential()                           #initialize the RNN
#adding input layerand the LSTM layer 
regressor.add(LSTM(units=4,activation='sigmoid',input_shape=(None,1)))


regressor.add(Dense(units=1))                          #adding output layers

regressor.compile(optimizer='adam',loss='mean_squared_error') #compiling the RNN

#fitting the RNN to the training set  
regressor.fit(xtrain,ytrain,batch_size=32,epochs=4000)     

# Reading CSV file into test set
test_set = pd.read_csv('test.csv')
test_set.head() 


real_stock_price = test_set.iloc[:,1:2]         #selecting the second column

real_stock_price = real_stock_price.values      #converting to 2D array

#getting the predicted BTC value of the first week of Dec 2017  
inputs = real_stock_price			
inputs = sc.transform(inputs)
inputs = np.reshape(inputs, (8, 1, 1))
predicted_stock_price = regressor.predict(inputs)
predicted_stock_price = sc.inverse_transform(predicted_stock_price)  


plt.plot(real_stock_price, color = 'red', label = 'Real BTC Value')
plt.plot(predicted_stock_price, color = 'blue', label = 'Predicted BTC Value')
plt.title('BTC Value Prediction')
plt.xlabel('Days')
plt.ylabel('BTC Value')
plt.legend()
plt.show()  