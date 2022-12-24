#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


bike_data = pd.read_csv("F:\daily_bike_share.csv")
bike_data.head()


# In[3]:


bike_data['day'] = pd.DatetimeIndex(bike_data['dteday']).day

bike_data.head(32)


# In[4]:


numeric_features= ['temp','atemp','hum','windspeed']
bike_data[numeric_features + ['casual']].describe()


# In[5]:


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# In[6]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


label=bike_data['casual']


# In[8]:


fig, ax = plt.subplots(2, 1, figsize = (9,12))
ax[0].hist(label, bins=100)
ax[0].set_ylabel('Frequency')
ax[0].axvline(label.mean(), color='magenta', linestyle='dashed', linewidth=2)
ax[0].axvline(label.median(), color='cyan', linestyle='dashed', linewidth=2)

ax[1].boxplot(label, vert=False)
ax[1].set_ylabel('casual')

fig.suptitle('Rental Distribution')
plt.show()


# In[9]:


for col in numeric_features:
    fig = plt.figure(figsize=(9,6))
    ax=fig.gca()
    feature = bike_data[col]
    feature.hist(bins=100, ax = ax)
    ax.axvline(feature.mean(), color='magenta', linestyle='dashed', linewidth = 2)
    ax.axvline(feature.median(), color='cyan', linestyle='dashed', linewidth = 2)
plt.show()
    


# In[10]:


import numpy as np


# In[19]:


categorical_features = ['season', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit','day']
for col in categorical_features:
    counts = bike_data[col].value_counts().sort_index()
    fig = plt.figure(figsize=(9,6))
    ax = fig.gca()
    counts.plot.bar(ax=ax, color='steelblue')
    ax.set_title(col + 'counts')
    ax.set_xlabel(col)
    ax.set_ylabel("Frequency")
plt.show()
X, y = bike_data(col).values

# Split data 70%-30% into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

print ('Training Set: %d rows\nTest Set: %d rows' % (X_train.shape[0], X_test.shape[0]))


# In[ ]:





# In[ ]:


for col in categorical_features:
    fig = plt.figure(figsize=(9,6))
    ax= fig.gca()
    bike_data.boxplot(column = 'casual', by = col, ax = ax)
    ax.set_title('Label by' + col)
    ax.set_xlabel("Bike Rentals")
    ax.set_ylabel("Feature")
plt.show()


# In[ ]:


X, y = bike_data[['season','mnth', 'holiday','weekday','workingday','weathersit','temp', 'atemp', 'hum', 'windspeed']].values, bike_data['casual'].values
print('Feature:' , X[:10], '\nLables:' , y[:10], sep='\n')


# In[ ]:





# In[ ]:




