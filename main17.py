# questions 2
# questions 1

import pandas as pd
import numpy as np
import warnings
import matplotlib.pyplot as plt
import matplotlib as mpl

# Filter for Belgium
be_consumption =food_consumption[food_consumption['country'] == 'Belgium']

# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# Calculate mean and median consumption in Belgium
print(np.mean(be_consumption['consumption']))
print(np.median(be_consumption['consumption']))

# Calculate m)an and median consumption in USA
print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))

# questions 5
import matplotlib.pyplot as plt

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# questions 4
# Histogram of co2_emission for rice and show plot
rice_consumption.co2_emission.hist()
plt.show()

# questions 6 the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 6)))

# questions 7 the variance and standard deviation of co2_emission
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

# questions 8 the histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption['food_category']=='beef'].hist()
