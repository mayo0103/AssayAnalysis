"""
Papiya Sen

  Generating Linear regression models for two dependent variables and five predictor variables.
  
  Dependent variables are raw material impurities. Predcitor variables are the particle size distribution.

"""

import csv

y1 = []
y2 = []
Mesh40 = []
Mesh100 = []
Mesh200 = []
Mesh325 = []
Mesh325Less = []

# Input data for this file consists of raw material assay and 5 particle size distribution categories
f = open("SparPSD.csv", "r")
reader = csv.DictReader(f)
for row in reader:
    y1.append(float(row["Assay"]))
    Mesh40.append(float(row["+40"]))
    Mesh100.append(float(row["+100"]))
    Mesh200.append(float(row["+200"]))
    Mesh325.append(float(row["+325"]))
    Mesh325Less.append(float(row["-325"]))
    
print y1
print Mesh40
print Mesh100
print Mesh200

# Input data for this file consists of raw material assay
f1 = open("SparData2.csv", "r")
reader1 = csv.DictReader(f1)
for row1 in reader1:
    y2.append(float(row1['Impurity2']))
    
# Removing extra rows from y2
del y2[52:63]


# Starting multivariate regression

import numpy as np
import statsmodels.api as sm

# Defining dependent variable
# Reshaping the data to columns

y = np.matrix(y2).T

# Defining independent variables
# Reshape the data to columns

x1 = np.matrix(Mesh40).T
x2 = np.matrix(Mesh100).T
x3 = np.matrix(Mesh200).T
x4 = np.matrix(Mesh325).T
x5 = np.matrix(Mesh325Less).T

# Put columns together to create input matrix
x = np.column_stack([x1,x2,x3,x4,x5])

# Generating regression model
X = sm.add_constant(x)
model = sm.OLS(y,X)
fn = model.fit()

print 'Intercept:', fn.params[5]
print 'Coefficients:', fn.params[0:5]
print 'p-value:', fn.pvalues
print 'R-sq:', fn.rsquared

