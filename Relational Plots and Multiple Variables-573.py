## 1. Introduction ##

import pandas as pd
import matplotlib.pyplot as plt
housing = pd.read_csv('housing.csv')
housing.head()
housing.tail()
housing.info()

## 2. Seaborn ##

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
housing = pd.read_csv('housing.csv')

sns.set_theme() #set visual properties to Seaborn defaults
sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice')
plt.show()

## Inspect the scatter plot and determine the correlation type
correlation  = 'positive'

## 3. Variable Representation: Color ##

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

housing = pd.read_csv('housing.csv')
sns.set_theme()
sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice', hue='Overall Qual', palette='RdYlGn')
plt.show()

## Sentence evaluation (eploratory analysis)
sentence_1 = True
sentence_2 = True

## 4. Variable Representation: Size ##

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

housing = pd.read_csv('housing.csv')
# sns.set_theme()
# sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice',
#             hue='Overall Qual', palette='RdYlGn')
# plt.show()

# *** *** *** *** *** *** *** *** *** ***

# Solution Code
sns.set_theme()
sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice',
            hue='Overall Qual', palette='RdYlGn', size='Garage Area', sizes=(1,300))
plt.show()

## Exploratory analysis - sentence evaluation
sentence_1 = False
sentence_2 = True

## 5. Variable Representation: Shape ##

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

housing = pd.read_csv('housing.csv')
# sns.set_theme()
# sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice',
#             hue='Overall Qual', palette='RdYlGn',
#             size='Garage Area', sizes=(1,300))
# plt.show()

# *** *** *** *** *** *** *** *** *** ***

# Solution Code
sns.set_theme()
sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice', 
            hue='Overall Qual', palette='RdYlGn',
            size='Garage Area', sizes=(1,300), 
            style='Rooms')
plt.show()

## Exploratory analysis - sentence evaluation
sentence_1 = False
sentence_2 = False

## 6. Variable Representation: Spatial Separation ##

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

housing = pd.read_csv('housing.csv')
# sns.set_theme()
# sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice',
#             hue='Overall Qual', palette='RdYlGn',
#             size='Garage Area', sizes=(1,300),
#             style='Rooms')
# plt.show()

## *** *** *** *** *** ***
## Solution Code
sns.set_theme()
sns.relplot(data=housing, x='Gr Liv Area', y='SalePrice',
            hue='Overall Qual', palette='RdYlGn',
            size='Garage Area', sizes=(1,300),
            style='Rooms', col='Year')
plt.show()

## Exploratory analysis - sentence evaluation
sentence_1 = True
sentence_2 = True