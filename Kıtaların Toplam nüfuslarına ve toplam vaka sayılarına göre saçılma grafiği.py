import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("coronavirus.csv")
plt.figure(figsize=(15, 7))
sns.scatterplot(x='Population', y='Total Cases', size='Total Cases', hue='Continent', data=data, sizes=(50, 200), palette='Set2')
plt.title('Nüfus ve Toplam Vakalar Arasındaki İlişki')
plt.xlabel('Nüfus')
plt.ylabel('Toplam Vaka Sayısı')
plt.legend(title='Kıta', bbox_to_anchor=(1, 1))
plt.show()