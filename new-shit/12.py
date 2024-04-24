import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('visitors.csv')

food_counts = df['food '].value_counts()

mode_rating = df['food '].mode()[0]

explode = [0.1 if i == mode_rating else 0 for i in food_counts.index]

food_counts.plot.pie(autopct='%1.1f%%', explode=explode)

plt.title('Pie Chart for Food Ratings')

plt.show()