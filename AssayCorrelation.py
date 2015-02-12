# -*- coding: utf-8 -*-
"""
Papiya Sen

  Testing for Correlation between impurity concentrations in a raw material. 
  
"""

import csv
import matplotlib.pyplot as plt
import numpy
from scipy import stats

y1 = []
y2 = []
y3 = []
y4 = []
mylist1 = []
mylist2 = []

# Input data consists of raw material assay and 4 impurities in comma-separated values  
f = open("SparData2.csv", "r")
reader = csv.DictReader(f)
for row in reader:
    temp1 = float(row['Impurity1'])
    temp2 = float(row['Assay'])
    temp3 = float(row['Impurity2'])
    temp4 = float(row['Impurity3'])
    y1.append(temp2)
    y2.append(temp3)
    y3.append(temp1)    
    y4.append(temp4)
    mylist1.append([temp3, temp1])
    mylist2.append([temp3, temp4])

# Creating 2-D array of impurities
x = numpy.array(mylist1).T
y = numpy.array(mylist2).T
print x

# calculate covariance of Impurities 1 and 2
a = numpy.cov(x)
print a

# calculate correlation of Impurities 1 & 2 and Impurities 2 & 3
z = numpy.corrcoef(x)
m = numpy.corrcoef(y)
print z
print m

# create scatter plot for impurities
plt.plot(y3, "g^", y2, "ro", y4, "b--")
plt.ylabel("==> %")
plt.xlabel("==> Time")
plt.show

# Generating regression model
slope, intercept, r_value, p_value, std_err = stats.linregress(y3, y4)
print "r_sq", r_value**2
print "p_val", p_value
