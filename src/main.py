#%%

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
# %%
# Import train and test data from CSV
df_total = pd.read_csv("../data/DailyDelhiClimate.csv", parse_dates=True, index_col="date")


# %%
df_total.head()

df_total.describe()

#%%
# Visualization of input data before preparation

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
# Data preparation

## Detection and removal of outliers
q_low = df_total["meanpressure"].quantile(0.01)
q_hi  = df_total["meanpressure"].quantile(0.99)

df_filtered_total = df_total[(df_total["meanpressure"] < q_hi) & (df_total["meanpressure"] > q_low)]



#%%
##Normalization
df_filtered_total['meanpressure'] = np.log2(df_filtered_total['meanpressure'])


#%%
#Standardization of data

scaler = StandardScaler()

standardized_data = scaler.fit_transform(df_filtered_total)

print(standardized_data)

# %%
