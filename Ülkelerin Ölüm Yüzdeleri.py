import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("coronavirus.csv")
etiket = data["Continent"]
top = data.groupby('Continent')['Death percentage'].sum()
pasta_uzaklik = [0.1,0,0,0,0,0]
plt.pie(top , labels=etiket.value_counts().index ,autopct='%1.1f%%', explode=pasta_uzaklik)
plt.title("Ülkelerin Ölüm Yüzdeleri")
plt.show()