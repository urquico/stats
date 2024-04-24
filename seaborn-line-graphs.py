import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Data-Visualization/bertdata.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(x='days', y='berttips', data=df, marker='o')
plt.title('Line Graph (seaborn module)')
plt.xlabel('Days')
plt.ylabel('BERT Tips')

# Display the plot
plt.show()