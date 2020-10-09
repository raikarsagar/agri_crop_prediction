#importing the required libraries
import pandas as pd
import numpy as np
# from sklearn.model_selection import train_test_split
import urllib.request
import json
import time
import pickle
import sys

model_filename = sys.argv[1]


# Load from file
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# these are the inputs to model (features)
temperature = str(31.61960395)
humidity = str(51.08614902)
ph = str(6.583213487)
rainfall = str(135.2358305) #this is not considered for prediction as of now

l=[]

l.append(temperature)
l.append(humidity)
l.append(ph)
# print(l)
print("pH of the soil is: ",ph)

predictcrop=[l]

# here the minimum threshold for ph is checked
if (ph<str(5.5)):
    print("The soil is deficient of nutrients but has minerals")
elif (str(5.5)<ph<str(8)):
    print("The soil has enough nutrients")
else:
    print("The soil is deficient of nutrients and minerals")


# Putting the names of crop in a single list
crops=['wheat','mungbean','Tea','millet','maize','lentil','jute','cofee','cotton','ground nut','peas',\
    'rubber','sugarcane','tobacco','kidney beans','moth beans','coconut','blackgram','adzuki beans',\
    'pigeon peas','chick peas','banana','grapes','apple','mango','muskmelon','orange','papaya','watermelon',\
    'pomegranate']

cr='rice'  # rice is the defalut predicted crop if the model doesnot return any valid prediction

#Predicting the crop
predictions = model.predict(predictcrop)
count=0
for i in range(0,30):
    if(predictions[0][i]==1):
        c=crops[i]
        count=count+1
        break;
    i=i+1
if(count==0):
    print('The predicted crop is %s'%cr)
else:
    print('The predicted crop is %s'%c)
