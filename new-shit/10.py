import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('visitors.csv')

plt.plot(df['bill'], marker='o')

plt.title('Line Graph for Bill')
plt.xlabel('Index')
plt.ylabel('Bill')

plt.show()