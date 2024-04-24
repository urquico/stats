import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt

# Import data from `bertdata.csv` inside `Data-Visualization` folder
data = pd.read_csv('Data-Visualization/bertdata.csv')

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

# Create bar graph on the first subplot
data.plot.bar(x='berttips', y='days', ax=ax1)
ax1.set_xlabel('berttips')
ax1.set_ylabel('days')
ax1.set_title('Bar Graph')

# Create line plot on the second subplot
sns.lineplot(x='berttips', y='days', data=data, linestyle=None, ax=ax2)
ax2.set_xlabel('berttips')
ax2.set_ylabel('days')
ax2.set_title('Line Graph')

# Adjust the layout and spacing between subplots
plt.tight_layout()

# Display the figure with both graphs
plt.show()
