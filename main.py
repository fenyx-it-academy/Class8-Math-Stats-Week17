
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (10, 8)

#read the data
food_consumption = pd.read_csv('food_consumption.csv', index_col=0)
food_consumption.head()

print (food_consumption)
print ('_____________________________________________________________________')
print ('Filter for Belgium')
print ('_____________________________________________________________________')

#filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']
print (be_consumption)

print ('_____________________________________________________________________')
print ('Filter for USA')
print ('_____________________________________________________________________')
# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']
print (usa_consumption)
print ('_____________________________________________________________________')

# Q-1) Calculate mean and median consumption in Belgium
print ('Q-1) Calculate mean and median consumption in Belgium')
BE_mean_consumption = be_consumption['consumption'].mean()
BE_median_consumption = be_consumption['consumption'].median()

print('Mean consumption in Belgium:', BE_mean_consumption)
print('Median consumption in Belgium:', BE_median_consumption)
print ('_____________________________________________________________________')

# Q-2) Calculate mean and median consumption of USA
print ('Q-2) Calculate mean and median consumption of USA')
USA_mean_consumption = usa_consumption['consumption'].mean()
USA_median_consumption = usa_consumption['consumption'].median()

print('Mean consumption in the USA:', USA_mean_consumption)
print('Median consumption in the USA:', USA_median_consumption)
print ('_____________________________________________________________________')


# Work with both countries together
be_and_usa = food_consumption[(food_consumption['country'] == 'Belgium') | 
                              (food_consumption['country'] == 'USA')]

# Q-3) Group by country, select consumption column, and compute mean and median
print ('Q-3) Group by country, select consumption column, and compute mean and median')

consumption_stats = be_and_usa.groupby('country')['consumption'].agg(['mean', 'median'])
print(consumption_stats)
print ('_____________________________________________________________________')

rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

#Q-4)Plot the histogram of co2_emission for rice
print ('Q-4)Plot the histogram of co2_emission for rice')

plt.hist(rice_consumption['co2_emission'])
plt.title('Histogram of CO2 emission for rice consumption')
plt.xlabel('CO2 emission')
plt.ylabel('Counts') # not sure if this is correct?
plt.show()

print ('_____________________________________________________________________')

#Q-5) Calculate mean and median of co2_emission with .agg()
print ('Q-5) Calculate mean and median of co2_emission with .agg()')

rice_co2_stats = rice_consumption['co2_emission'].agg(['mean', 'median'])
print('Mean CO2 emission:', rice_co2_stats['mean'])
print('Median CO2 emission:', rice_co2_stats['median'])
print ('_____________________________________________________________________')

#Q-6) Calculate the quintiles of co2_emission
print ('Q-6) Calculate the quintiles of co2_emission')
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 6)))

print ('_____________________________________________________________________')

#Q-7) Calculate the variance and standard deviation of co2_emission for food_categories
print ('Q-7) Calculate the variance and standard deviation of co2_emission for food_categories')

co2_stats = food_consumption.groupby('food_category')['co2_emission'].agg(['var', 'std'])
print(co2_stats)

print ('_____________________________________________________________________')



#Q-8) Create histogram of co2_emission for food_category 'beef'
print ("Q-8) Create histogram of co2_emission for food_category 'beef'")

# Filter for beef consumption
beef_consumption = food_consumption[food_consumption['food_category'] == 'beef']

plt.hist(beef_consumption['co2_emission'])
plt.title('Histogram of CO2 emission for beef consumption')
plt.xlabel('CO2 emission')
plt.ylabel('Counts')
plt.show()

print ('_____________________________________________________________________')

emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()

print(emissions_by_country)

print ('_____________________________________________________________________')

q1 = np.quantile(emissions_by_country, 0.25)
q3 = np.quantile(emissions_by_country, 0.75)
iqr = q3 - q1

# Calculate the lower and upper cutoffs for outliers
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

# Subset emissions_by_country to find outliers
outliers = emissions_by_country[(emissions_by_country > upper) | (emissions_by_country < lower)]
print(outliers)

