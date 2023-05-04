import csv 
import matplotlib.pyplot as plt
from scipy.stats import beta
import numpy as np
import math

prior_alpha = 1
prior_beta = 1
num_heads = 7
num_tails = 3


def bayes_theorem( p_b_given_a , p_b_given_not_a):

     p_not_a = 1 - 0.01
     p_b = p_b_given_a * 0.01 +p_b_given_not_a * p_not_a
     p_a_given_b = (p_b_given_a * 0.01) / p_b
     return p_a_given_b
        
with open("food_consumption.csv",'r') as file : 
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row[3] , type(row[3]))
        p_b_given_as = row[3]
        print('\t',row[4],type(row[4]))
        p_b_given_not_as = row[4]
        result = bayes_theorem(5,6)
        print(f"the probability is : {result:.3f}")


p_no = 1 - 0.01
p_b = 5 * 0.01
p_n_b = 3 * p_no

labels = ['positive','negative']
positive_given = [p_b , p_n_b ]
negative_given = [0.01 - p_b , p_no - p_n_b ]

fig , ax = plt.subplots()

bar_width = 0.35
x = np.arange(len(labels))

ax.bar(x, positive_given, bar_width, label='P', color='blue', edgecolor='k')
ax.bar(x + bar_width, negative_given, bar_width, label='N', color='orange', edgecolor='k')

ax.text(0, p_b/ 2, f"{result:.3f}", fontsize=12, color='white', ha='center')


ax.set_xticks(x + bar_width / 2)
ax.set_xticklabels(labels)
ax.set_ylabel('Probability')
ax.legend()

plt.show()



posterior_alpha = prior_alpha + num_heads
posterior_beta = prior_beta + num_tails
x = np.linspace(0, 1, 1000)
prior_pdf = beta.pdf(x, prior_alpha, prior_beta)
posterior_pdf = beta.pdf(x, posterior_alpha, posterior_beta)

plt.figure(figsize=(10, 6))
plt.plot(x, prior_pdf, label='Prior (α=1, β=1)', lw=2)
plt.plot(x, posterior_pdf, label='Posterior (α=8, β=4)', lw=2)
plt.xlabel('Probability of Heads')
plt.ylabel('Probability Density')
plt.legend()
plt.title('food consumption')
plt.show()
