import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Data-Visualization/bertdata.csv')

plt.figure(figsize=(10, 6))
sns.barplot(x='days', y='berttips', data=df)

plt.title('Bar Graph (seaborn module)')
plt.xlabel('Days')
plt.ylabel('BERT Tips')

plt.show()