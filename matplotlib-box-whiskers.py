import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Data-Visualization/bertdata.csv')

plt.figure(figsize=(10, 6))
plt.boxplot(df['berttips'], vert=False)
plt.title('Box and Whisker Plot (matplotlib module)')
plt.xlabel('BERT Tips')
plt.show()