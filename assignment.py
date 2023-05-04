import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10, 8)


# read the data
food_consumption = pd.read_csv(
    'G:/Fenyx/Week-17/food_consumption.csv', index_col=0)
food_consumption.head()

# filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium']

# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA']

#Q1 and Q2
print("Belguim mean consumption is:",be_consumption['consumption'].mean())
print("Belguim median consumption is:",be_consumption['consumption'].median())
print("USA mean consumption is:",usa_consumption['consumption'].mean())
print("USA median consumption is:",usa_consumption['consumption'].median())

#Q3 
be_and_usa = food_consumption[(food_consumption['country'] == 'Belgium') |
                              (food_consumption['country'] == 'USA')]
df = pd.DataFrame(
    {'country': be_and_usa['country'], 'consumption': be_and_usa['consumption']})
print(df.groupby(['country']).agg(['mean', 'median']))


#Q4
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']
plt.hist(rice_consumption['co2_emission'])
plt.show()

#Q5
print(rice_consumption['co2_emission'].agg(['mean', 'median']))

#Q6 
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 6)))

#Q7 
food = food_consumption[['food_category', 'co2_emission']]
print(food.groupby(['food_category']).agg(['var', 'std']))

#Q8
beef_consumption = food_consumption[food_consumption['food_category'] == 'beef']
plt.hist(beef_consumption['co2_emission'])
plt.show()

