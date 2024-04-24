import pandas as pd

df = pd.read_csv('visitors.csv')

food_summary = df.groupby('gender')['food '].value_counts()
service_summary = df.groupby('gender')['service'].value_counts()

print("Food Summary:")
print(food_summary)
print("\nService Summary:")
print(service_summary)