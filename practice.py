# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# plt.rcParams['figure.figsize'] = (10, 8)
# #read the data
# #./dataset/ is a path. Copy and paste the path of the CSV file in your computer to read the data. 
# food_consumption = pd.read_csv('./food_consumption.csv', index_col=0)
# #print(food_consumption.head())
# #filter for Belgium
# be_consumption = food_consumption[food_consumption['country'] == 'Belgium']
# #print(be_consumption)
# # Filter for USA
# usa_consumption = food_consumption[food_consumption['country'] == 'USA']

# #Q-1) Calculate mean and median consumption in Belgium
# rows=[]
# sum =0
# for index,row in enumerate(be_consumption['consumption']): 
#     sum += row
#     rows.append(row)
# mean = sum/(index +1)
# median = rows[(index+1)//2]
# print(f"the mean consumption in Belgium is =  {mean} ")
# print(f"the median for  consumption in Belgium is =  {median} ")


# #Q-2) Calculate mean and median consumption of USA
# rows=[]
# sum =0
# for index,row in enumerate(usa_consumption['consumption']): 
#     sum += row
#     rows.append(row)
# mean = sum/(index +1)
# median = rows[(index+1)//2]
# print(f"the mean consumption in USA is =  {mean} ")
# print(f"the median for  consumption in USA is =  {median} ")

# # Q-3) Group by country, select consumption column, and compute mean and median
# # the result is the same with Q-2)

# rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# #Q-4)Plot the histogram of co2_emission for rice

# #Q-5) Calculate mean and median of co2_emission with .agg()

