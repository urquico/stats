import pandas as pd

df = pd.read_csv('visitors.csv')

summary = df['bill'].describe()

print(summary)