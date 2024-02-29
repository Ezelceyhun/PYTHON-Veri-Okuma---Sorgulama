import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("coronavirus.csv")
plt.figure(figsize=(12, 6))
sns.barplot(x='Tot Cases//1M pop', y='Continent', data=data, palette={'Asia': 'orange', 'Northern America': 'skyblue', 'Europe': 'green','Africa':'blue', 'Latin America and the Caribbean':'red', 'Oceania':'purple'})
plt.title('Kıtalara Göre 1 Milyonda ki Toplam Vaka Sayısı')
plt.xlabel('Toplam Vaka Sayısı')
plt.show()