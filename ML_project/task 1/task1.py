# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:32:40 2021

@author: OsamaAyman
"""


#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#read dataset
dataset=pd.read_csv('Wuzzuf_Jobs.csv')
dataset.describe()

#print dataset
dataset

#-------------------------------------------------

#sorting dataset

dataset.sort_values("Company", inplace = True)

# dropping all duplicate values

dataset.drop_duplicates(subset='Company', keep="first", inplace = True)
dataset.sort_values("Company", inplace = True)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp_mean = imp_mean.fit(x[:, 0:3])
x[:, 0:3] = imp_mean.transform(x[:, 0:3])
print(x)

#-----------------------------------------------

#Q4

import pandas as pd
data1=pd.read_csv('Wuzzuf_Jobs.csv')
company_counts=data1['Company'].value_counts()
print('the most demanding companies for jobs are :')
print(company_counts.index[0:5])

#Q5

from matplotlib import pyplot as plt
plt.pie(company_counts)
plt.show()
print('the most demanding companies for jobs are :')
print(company_counts.index[0:5])

#-----------------------------------------------

#Q6

import pandas as pd
data2=pd.read_csv('Wuzzuf_Jobs.csv')
title_counts=data2['Title'].value_counts()
print('the most popular job titles are :')
print(title_counts.index[0:5])

#Q7

from matplotlib import pyplot as plt
plt.bar(title_counts.index[0:3], title_counts[0:3], color ='red',
		width = 0.4)
plt.xlabel("Jobs Title")
plt.ylabel("Number Of Job Titles")
plt.title("The Most Pouplar Jobs Title")
plt.show()
print('the most popular job titles are :')
print(title_counts.index[0:5])

#-----------------------------------------------

#Q8

import pandas as pd
data3=pd.read_csv('Wuzzuf_Jobs.csv')
location_counts=data3['Location'].value_counts()
print('the most popular Areas are :')
print(location_counts.index[0:5])

#Q9

from matplotlib import pyplot as plt
plt.bar(location_counts.index[0:5], location_counts[0:5], color ='red',
		width = 0.4)
plt.xlabel("Areas")
plt.ylabel("Count Of Areas")
plt.title("The Most Pouplar Areas")
plt.show()
print('the most popular Areas are :')
print(location_counts.index[0:5])

#----------------------------------------------

#Q10

import pandas as pd
data4=pd.read_csv('Wuzzuf_Jobs.csv')
skills_counts=data4['Skills'].value_counts()
m=pd.DataFrame(skills_counts)
display(m)
print('The Most Important Skills are :')
print(m[0:3])

#-----------------------------------------------