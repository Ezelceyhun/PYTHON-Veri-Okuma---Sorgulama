import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("coronavirus.csv")
plt.figure(figsize=(12, 6))
ulke_kisalt = data["Country"][110:115]
sns.barplot(x=ulke_kisalt, y='Total Cases', data=data, color='skyblue', label='Toplam Vakalar')
sns.barplot(x=ulke_kisalt, y='Total Deaths', data=data, color='salmon', label='Toplam Ölümler')
plt.title('Ülkelerin Nüfuslarına Göre Toplam Vaka ve Ölüm Sayıları')
plt.legend()
plt.xticks(rotation=45)
plt.show()