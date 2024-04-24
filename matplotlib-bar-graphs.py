import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data-Visualization/bertdata.csv')

berttips = df['berttips']
days = df['days']

plt.figure(figsize=(10, 6))
plt.bar(days, berttips)

plt.title('Bar Graph (matplotlib module)')
plt.xlabel('Days')
plt.ylabel('BERT Tips')

plt.show()