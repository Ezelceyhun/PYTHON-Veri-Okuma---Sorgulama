import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("coronavirus.csv")
plt.figure(figsize=(10, 6))
plt.bar(data['Continent'][:3], data['Total Cases'][:3])
plt.title('En Fazla Vakaya Sahip 3 Ülke')
plt.xlabel('Ülkeler')
plt.ylabel('Toplam Vakalar (Milyon Cinsinden)')
plt.show()