import matplotlib.pyplot as plt
import pandas as pd

# use data from `bertdata.csv` inside `Data-Visualization` folder
data = pd.read_csv('Data-Visualization/bertdata.csv')

# Create a figure and axis
fig, ax = plt.subplots()

# Create the box and whiskers plot using 'berttips' and 'days' columns
ax.boxplot([data['berttips'], data['days']])

# Set the title and labels
ax.set_title('Box and Whiskers Plot')
ax.set_xlabel('Data')
ax.set_ylabel('Values')

# Show the plot
plt.show()