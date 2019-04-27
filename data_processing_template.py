# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

#Import dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values 
y = dataset.iloc[:,3].values

# Splitting the dataset into the Training set and test set 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)

#Feature Scaling 
"""from sklearn.preprocessing import  StandardScaler 
sc_X = StandardScaler();
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""
