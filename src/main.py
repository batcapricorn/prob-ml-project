#%%

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# %%
# Import data from CSV file
df_total = pd.read_csv("../data/DailyDelhiClimate.csv", parse_dates=True)


# %%
df_total.head()

df_total.describe()

#%%
# Visualization of input data before preparation

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

#%%
#Boxplot for detection of outliers

fig, ax = plt.subplots(1, 4, figsize=(30, 10))

# draw boxplots - for one column in each subplot
df_total.boxplot('meantemp', ax=ax[0])
df_total.boxplot('humidity', ax=ax[1])
df_total.boxplot('wind_speed', ax=ax[2])
df_total.boxplot('meanpressure', ax=ax[3])

plt.subplots_adjust(wspace=0.5) 

plt.show()


#%%
# Data preparation

## Removal of outliers
q_low = df_total["meanpressure"].quantile(0.01)
q_hi  = df_total["meanpressure"].quantile(0.99)

df_filtered_total = df_total[(df_total["meanpressure"] < q_hi) & (df_total["meanpressure"] > q_low)]



#%%
##Normalization
df_filtered_total['meanpressure'] = np.log2(df_filtered_total['meanpressure'])


#%%
#Standardization of data

scaler = StandardScaler()

df_standardized_data = scaler.fit_transform(df_filtered_total)

print(df_standardized_data)
