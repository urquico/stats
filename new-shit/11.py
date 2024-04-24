import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('visitors.csv')

plt.boxplot(df['bill'])

plt.title('Box and Whiskers Plot for Bill')
plt.ylabel('Bill')

plt.show()