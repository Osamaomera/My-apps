#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


# task 2 Q1
# Importing the dataset
dataset = pd.read_csv(r'C:\Users\OsamaAyman\Desktop\ML_project\task 2\Wuzzuf_Jobs.csv')
# fatorize
dataset['Fact']=pd.factorize(dataset['YearsExp'])[0]
dataset


# In[3]:


# factorize YearsExp and Company inplace 
dataset = pd.read_csv(r'C:\Users\OsamaAyman\Desktop\ML_project\task 2\Wuzzuf_Jobs.csv')
dataset['YearsExp']=pd.factorize(dataset['YearsExp'])[0]
dataset['Company']=pd.factorize(dataset['Company'])[0]
dataset


# In[4]:


# draw Elbow Method between YearsExp and Company
dataset = pd.read_csv(r'C:\Users\OsamaAyman\Desktop\ML_project\task 2\Wuzzuf_Jobs.csv')
dataset['YearsExp']=pd.factorize(dataset['YearsExp'])[0]
dataset['Company']=pd.factorize(dataset['Company'])[0]
from sklearn.cluster import KMeans
X = dataset.iloc[:, [5, 1]].values
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# In[5]:


# the number of clusters is 4 from figure Elbow Method between YearsExp and Company
# so the k-meanning is :-
dataset = pd.read_csv(r'C:\Users\OsamaAyman\Desktop\ML_project\task 2\Wuzzuf_Jobs.csv')
dataset['YearsExp']=pd.factorize(dataset['YearsExp'])[0]
dataset['Company']=pd.factorize(dataset['Company'])[0]
from sklearn.cluster import KMeans
X = dataset.iloc[:, [5, 1]].values
print(X)
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)
y_kmeans == 0
# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'purple', label = 'Cluster 4')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'black', label = 'Centroids')
plt.title('Clusters of Companies with YearsExp')
plt.xlabel('Years Experinece')
plt.ylabel('Companies')
plt.legend()
plt.show()


# In[6]:


# Factroize Title and Company inplace  
dataset = pd.read_csv(r'C:\Users\OsamaAyman\Desktop\ML_project\task 2\Wuzzuf_Jobs.csv')
dataset['Title']=pd.factorize(dataset['Title'])[0]
dataset['Company']=pd.factorize(dataset['Company'])[0]
dataset


# In[7]:


# draw Elbow Method between jobs Title and Company
dataset = pd.read_csv(r'C:\Users\OsamaAyman\Desktop\ML_project\task 2\Wuzzuf_Jobs.csv')
dataset['Title']=pd.factorize(dataset['Title'])[0]
dataset['Company']=pd.factorize(dataset['Company'])[0]
from sklearn.cluster import KMeans
X = dataset.iloc[:, [0, 1]].values
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# In[8]:


# the number of clusters is 5 from figure Elbow Method between job Titles and Company
# so the k-meanning is :-
dataset = pd.read_csv(r'C:\Users\OsamaAyman\Desktop\ML_project\task 2\Wuzzuf_Jobs.csv')
dataset['Title']=pd.factorize(dataset['Title'])[0]
dataset['Company']=pd.factorize(dataset['Company'])[0]
from sklearn.cluster import KMeans
X = dataset.iloc[:, [0, 1]].values
print(X)
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(X)
y_kmeans == 0
# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'purple', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'orange', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'black', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Titles of jobs')
plt.ylabel('Companies')
plt.legend()
plt.show()

