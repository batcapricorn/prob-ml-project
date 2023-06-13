#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[ ]:


# Import train and test data from CSV

df_train = pd.read_csv("../data/DailyDelhiClimateTrain.csv", parse_dates=True)
df_test = pd.read_csv("../data/DailyDelhiClimateTest.csv", parse_dates=True)


# In[ ]:


df_train.head()
df_test.head()


# In[ ]:


df_train.describe()
# df_test.describe()


# In[ ]:


# Visualization of input data before preparation

df_total = df_train.append(df_test)

df_total = df_total.set_index('date')

fig = plt.figure(figsize=(30, 10))
rows = 2
columns = 2

ax1 = fig.add_subplot(rows, columns, 1)
ax1.set_title("Mean Temperature")
plt.ylabel('Classes')
df_total["meantemp"].plot()

ax1 = fig.add_subplot(rows, columns, 2)
ax1.set_title("Humidity")
df_total["humidity"].plot()

ax1 = fig.add_subplot(rows, columns, 3)
ax1.set_title("Wind Speed")
df_total["wind_speed"].plot()

ax1 = fig.add_subplot(rows, columns, 4)
ax1.set_title("Mean Pressure")
df_total["meanpressure"].plot()

plt.show()


# In[ ]:


# Data preparation

## Detection and removal of outliers
q_low_train = df_train["meanpressure"].quantile(0.01)
q_hi_train  = df_train["meanpressure"].quantile(0.99)

df_filtered_train = df_train[(df_train["meanpressure"] < q_hi_train) & (df_train["meanpressure"] > q_low_train)]

q_low_test = df_test["meanpressure"].quantile(0.01)
q_hi_test  = df_test["meanpressure"].quantile(0.99)

df_filtered_test = df_test[(df_test["meanpressure"] < q_hi_test) & (df_test["meanpressure"] > q_low_test)]



##Normalization
df_filtered_train['meanpressure'] = np.log2(df_filtered_train['meanpressure'])
df_filtered_test['meanpressure'] = np.log2(df_filtered_test['meanpressure'])

df_filtered_test.describe()

