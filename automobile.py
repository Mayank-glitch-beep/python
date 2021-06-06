# -*- coding: utf-8 -*-
"""
Code Challenge
  Name: 
      Exploratory Data Analysis - Automobile
  Filename: 
      EDA_Automobile.py
  Dataset:
      Automobile.csv
  Problem Statement:
      Perform the following task :
      1. Handle the missing values for Price column
      2. Get the values from Price column into a numpy.ndarray
      3. Calculate the Minimum Price, Maximum Price, Average Price and Standard Deviation of Price
      4. Make a pie chart for all car makers
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Automobile.csv")
df['price']=df['price'].fillna(df['price'].mean())
x=np.array(df['price'])

#minimum price
minimum=df['price'].min()

#maximum price
maximum=df['price'].max()

#averageprice
avgprice=df['price'].mean()

#Standard deviation
stand=df['price'].std()

mn=np.array(df['make'].unique())
vc=np.array(df['make'].value_counts())
fig1 ,ax1 = plt.subplots()
ax1.pie(vc, labels=mn, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

 

