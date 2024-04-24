import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Data-Visualization/bertdata.csv')

plt.figure(figsize=(10, 6))
sns.boxplot(x='berttips', data=df, orient='h')
plt.title('Box and Whisker Plot (seaborn module)')
plt.xlabel('BERT Tips')
plt.show()