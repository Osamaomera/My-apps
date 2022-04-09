# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# importing data :
data = pd.read_csv('Salary_Data.csv')

# Specializing Data :
x = data['YearsExperience']
y = data['Salary']
     
# Calculating Size and Mean Values :
N = len(x)
x_mean = x.mean()
y_mean = y.mean()

# Values of B0 and B1 :
B1_num = ((x - x_mean) * (y - y_mean)).sum()
B1_den = ((x - x_mean)**2).sum()
B1 = B1_num / B1_den

B0 = y_mean - (B1*x_mean)

# plotting line across points :
plt.plot(x, B0 + B1*x, c = 'r')
plt.scatter(x, y)
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression")
plt.show()


