import numpy as np 
import matplotlib.pyplot as plt

time_periods = ['T1', 'T2', 'T3', 'T4']
category_a = [30, 40, 20, 50]
category_b = [20, 35, 25, 40]
category_c = [10, 15, 30, 20]

bar1 = np.array(category_a)
bar2 = np.array(category_b)
bar3 = np.array(category_c)

plt.bar(time_periods, bar1, label='Category A')
plt.bar(time_periods, bar2, bottom=bar1, label='Category B')
plt.bar(time_periods, bar3, bottom=bar1+bar2, label='Category C')

plt.title('Stacked Bar Chart')
plt.xlabel('Time Period')
plt.ylabel('Value')
plt.legend()
plt.show()