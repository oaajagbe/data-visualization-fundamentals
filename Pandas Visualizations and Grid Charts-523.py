## 2. Traffic Behavior Dataset ##

import pandas as pd
traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic.head()
traffic.tail()
traffic.info()

## 3. Slowness in Traffic ##

import pandas as pd
import matplotlib.pyplot as plt
traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)
plt.hist(traffic['Slowness in traffic (%)'])
plt.show()

sentence_1 = True
sentence_2 = True
sentence_3 = False

## 4. Pandas Visualization Methods ##

import matplotlib.pyplot as plt
import pandas as pd
traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)

# Use the Series.plot.hist() method to generate a histogram for the Slowness in traffic (%) column.
traffic['Slowness in traffic (%)'].plot.hist()
plt.title('Distribution of Slowness in traffic (%)')
plt.xlabel('Slowness in traffic (%)')
plt.show()

## 5. Frequency of Incidents ##

import pandas as pd
import matplotlib.pyplot as plt

traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)

incidents = traffic.drop(['Hour (Coded)', 'Slowness in traffic (%)'],
                        axis=1)

## Generating a vertical plot makes the x-tick labels are very hard to read — we need to tilt our head to the left to be able to read anything.
## Therefore, generating a horizontal bar plot for the incidents.sum() table will be better
incidents.sum().plot.barh()
plt.show()

sentence_1 = False
sentence_2 = True
sentence_3 = True

## 6. Correlations with Traffic Slowness ##

import pandas as pd
import matplotlib.pyplot as plt

traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)

traffic.plot.scatter(x='Slowness in traffic (%)',
                     y='Lack of electricity')
plt.show()

## generate the other two scatter plots. Using the DataFrame.plot.scatter() method:

## Generate a scatter plot with Slowness in traffic (%) on the x-axis and Point of flooding on the y-axis
traffic.plot.scatter(x='Slowness in traffic (%)',
                     y='Point of flooding')
plt.show()

## Generate a scatter plot with Slowness in traffic (%) on the x-axis and Semaphore off on the y-axis. 
traffic.plot.scatter(x='Slowness in traffic (%)',
                     y='Semaphore off')
plt.show()

## 7. Traffic Slowness Over 20% ##

import pandas as pd
import matplotlib.pyplot as plt

traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)

# To look for more evidence, we're going to isolate all the rows where traffic slowness is 20% or more. Then, we're going to calculate and visualize the incident frequency.
slowness_20_or_more = traffic[traffic['Slowness in traffic (%)'] >= 20]
slowness_20_or_more = slowness_20_or_more.drop(['Slowness in traffic (%)', 'Hour (Coded)'], axis=1)
incident_frequencies = slowness_20_or_more.sum()
# incident_frequencies.plot.bar()
# plt.show()
incident_frequencies.plot.barh()
plt.show()

## 8. How Traffic Slowness Change ##

import pandas as pd
import matplotlib.pyplot as plt

traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
traffic_per_day = {}
for i, day in zip(range(0, 135, 27), days):
    each_day_traffic = traffic[i:i+27]
    traffic_per_day[day] = each_day_traffic
    
# generate a line plot for each day from the isolated data
## Create a separate line plot for each day by using a for loop. Iterate over the days list, and for each day
for day in days:
    traffic_per_day[day].plot.line(x='Hour (Coded)',
                                    y='Slowness in traffic (%)')
    plt.title(day)
    plt.ylim([0, 25]) # make the range of the y-axis the same for all plots — this helps with comparison
    plt.show()

## 9. Comparing Graphs ##

import pandas as pd
import matplotlib.pyplot as plt

traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
traffic_per_day = {}
for i, day in zip(range(0, 135, 27), days):
    each_day_traffic = traffic[i:i+27]
    traffic_per_day[day] = each_day_traffic
    
# generate this plot ourselves in the next exercise. 
## However, we're going to use plt.plot() instead of the DataFrame.plot.line() method. That's because DataFrame.plot.line() plots separate graphs by default, which means we won't be able to put all the lines on the same graph

# Generate all the five line plots on a single graph. Use a for loop over the days list
for day in days:
    plt.plot(traffic_per_day[day]['Hour (Coded)'], traffic_per_day[day]['Slowness in traffic (%)'], label=day)
    
#plt.title('Traffic Comparison Per Day')
#plt.xlabel('Hour (Coded)')
#plt.ylabel('Slowness in traffic (%)')
plt.legend()
plt.show()

## 10. Grid Charts ##

import pandas as pd
import matplotlib.pyplot as plt

traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)

plt.figure()
plt.subplot(3, 2, 1)
plt.subplot(3, 2, 2)
plt.subplot(3, 2, 6)
plt.subplot(3, 2, 3)
plt.subplot(3, 2, 4)
plt.subplot(3, 2, 5)
plt.show()

## 11. Grid Charts (II) ##

import pandas as pd
import matplotlib.pyplot as plt

traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
traffic_per_day = {}
for i, day in zip(range(0, 135, 27), days):
    each_day_traffic = traffic[i:i+27]
    traffic_per_day[day] = each_day_traffic
    
plt.figure(figsize=(10,12))
for i, day in zip(range(1, 6), days):
    plt.subplot(3, 2, i)
    plt.plot(traffic_per_day[day]['Hour (Coded)'], traffic_per_day[day]['Slowness in traffic (%)'])
    plt.title(day)
    plt.ylim([0,25])
    
plt.show()

## 12. Grid Charts (III) ##

import pandas as pd
import matplotlib.pyplot as plt

traffic = pd.read_csv('traffic_sao_paulo.csv', sep=';')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].str.replace(',', '.')
traffic['Slowness in traffic (%)'] = traffic['Slowness in traffic (%)'].astype(float)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
traffic_per_day = {}
for i, day in zip(range(0, 135, 27), days):
    each_day_traffic = traffic[i:i+27]
    traffic_per_day[day] = each_day_traffic
    
plt.figure(figsize=(10,12))

for i, day in zip(range(1,6), days):
    plt.subplot(3, 2, i)
    plt.plot(traffic_per_day[day]['Hour (Coded)'],
        traffic_per_day[day]['Slowness in traffic (%)'])
    plt.title(day)
    plt.ylim([0,25])
    
plt.subplot(3, 2, 6)
for day in days:
    plt.plot(traffic_per_day[day]['Hour (Coded)'], traffic_per_day[day]['Slowness in traffic (%)'], label=day)
    plt.ylim([0,25])
plt.legend()
plt.show()