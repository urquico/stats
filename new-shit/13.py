import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('visitors.csv')

service_counts = df['service'].value_counts()

mode_rating = df['service'].mode()[0]

explode = [0.1 if i == mode_rating else 0 for i in service_counts.index]

service_counts.plot.pie(autopct='%1.1f%%', explode=explode)

plt.title('Pie Chart for Service Ratings')

plt.show()