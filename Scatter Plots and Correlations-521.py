## 1. Bike Sharing Time Series ##

import pandas as pd
bike_sharing = pd.read_csv('day.csv')
print(bike_sharing.head())
print(bike_sharing.tail())
bike_sharing.info()

## 2. Exploring Data ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])
plt.plot(bike_sharing['dteday'], bike_sharing['casual'], label='Casual')
plt.plot(bike_sharing['dteday'], bike_sharing['registered'], label='Registered')
plt.xticks(rotation=30)
plt.ylabel('Bikes Rented')
plt.xlabel('Date')
plt.title('Bikes Rented: Casual vs. Registered')
plt.legend()
plt.show()

## 3. Seasonal Trends ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])
plt.plot(bike_sharing['dteday'], bike_sharing['temp'], label='temperature')
plt.xticks(rotation=45)
# plt.legend()
plt.show()

## 4. Scatter Plots ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

## scatter plots
plt.scatter(bike_sharing['windspeed'], bike_sharing['cnt'])
plt.xlabel('Wind Speed')
plt.ylabel('Bikes Rented')
plt.show()

## 5. Correlation ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

## generate scatter plot
plt.scatter(bike_sharing['atemp'], bike_sharing['registered'])
plt.show()
correlation = 'positive'

## 6. Pearson Correlation Coefficient ##

sentence_1 = True
sentence_2 = True
sentence_3 = False
sentence_4 = True

## 7. Measuring Pearson's r ##

import pandas as pd
import matplotlib.pyplot as plt

bike_sharing = pd.read_csv('day.csv')
bike_sharing['dteday'] = pd.to_datetime(bike_sharing['dteday'])

## Calculate the Pearson's r between the temp and atemp columns
temp_atemp_corr = bike_sharing['temp'].corr(bike_sharing['atemp'])

## Calculate the Pearson's r between the windspeed and hum columns.
wind_hum_corr = bike_sharing['windspeed'].corr(bike_sharing['hum'])

## catter plot with the temp column on the x-axis and the atemp column on the y-axis
plt.scatter(bike_sharing['temp'], bike_sharing['atemp'])
plt.xlabel('Air Temperature')
plt.ylabel('Feeling Temperature')
plt.show()

## scatter plot with the windspeed column on the x-axis and the hum column on the y-axis
plt.scatter(bike_sharing['windspeed'], bike_sharing['hum'])
plt.xlabel('Wind Speed')
plt.ylabel('Humidity')
plt.show()

## 8. Categorical Columns ##

## Let's now do an exercise and continue the discussion on the next screen. We're going to use the weathersit column, which is categorical and has four unique values describing the weather:

# 1: clear or few clouds
# 2: mist or cloudy
# 3: light rain, light snow, thunderstorm
# 4: heavy rain, snow, ice pellets, fog

# bike_sharing['weathersit'].value.counts()
sentence_1 = True
sentence_2 = True
sentence_3 = True