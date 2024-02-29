import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("coronavirus.csv")
yuzde = (data['Total Deaths'] / data['Total Cases']) * 100
plt.figure(figsize=(12, 6))
sns.barplot(x='Continent', y=yuzde, hue='Population', data=data, palette='coolwarm')
plt.ylabel("Ölüm Oranı")
plt.xlabel("Kıtalar")
plt.title('Ülkelerin Nüfuslarına Göre Ölüm Yüzdesi')
plt.show()