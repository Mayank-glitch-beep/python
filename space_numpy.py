# -*- coding: utf-8 -*-

​
"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""
import numpy as np
list1=[]
for i in range(0,9):
    list1.append(int(input()))
x=np.array(list1)    
print("Input",x)
x1=x.reshape(3,3)
print("output",x1)
