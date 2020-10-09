#importing the required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import urllib.request
import json
import time
import pickle
import sys

data_filename = sys.argv[1]
pkl_filename = sys.argv[2]


#Reading the csv file
data=pd.read_csv(data_filename)
#print(data.head(1))

#Creating dummy variable for target i.e label
label= pd.get_dummies(data.label).iloc[: , 1:]

data= pd.concat([data,label],axis=1)
data.drop('label', axis=1,inplace=True)
#print('The data present in one row of the dataset is')
#print(data.head(1))
train_data=data.iloc[:, 0:3].values
train_label=data.iloc[: ,4:].values

#Dividing the data into training and test set
X_train,X_test,y_train,y_test=train_test_split(train_data,train_label,test_size=0.3)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Importing Decision Tree classifier
from sklearn.tree import DecisionTreeRegressor
model=DecisionTreeRegressor()

#Fitting the classifier into training set
model.fit(X_train,y_train)
pred=model.predict(X_test)

from sklearn.metrics import accuracy_score
# Finding the accuracy of the model
a=accuracy_score(y_test,pred)
print("The accuracy of this model is: ", a*100)

# Save to file in the current working directory

with open(pkl_filename, 'wb') as file:
    pickle.dump(model, file)


