import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# use data from `bertdata.csv` inside `Data-Visualization` folder
data = pd.read_csv('Data-Visualization/bertdata.csv')

# Create line plot using seaborn with linestyle as None
sns.lineplot(x='berttips', y='days', data=data, linestyle=None)

# Set plot title and labels
plt.title("Line Graph")
plt.xlabel("berttips")
plt.ylabel("days")

# Display the plot
plt.show()
