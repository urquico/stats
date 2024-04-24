import pandas as pd
import matplotlib.pyplot as plt

# import data from `bertdata.csv` inside `Data-Visualization` folder

data = pd.read_csv('Data-Visualization/bertdata.csv')

# Create a bar graph
data.plot.bar(x='berttips', y='days')

# Add labels and title
plt.xlabel('berttips')
plt.ylabel('days')
plt.title('Bar Graph')

# Display the graph
plt.show()
 