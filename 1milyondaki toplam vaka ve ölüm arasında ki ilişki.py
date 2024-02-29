import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("coronavirus.csv")
sinir_ulke=data["Country"][:20]
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Tot Cases//1M pop', y='Tot Deaths/1M pop', hue=sinir_ulke, size=sinir_ulke, data=data, sizes=(100, 100))
plt.title('1M^daki Toplam Vakalar ve 1M^daki Toplam Ölümler Arasındaki İlişki')
plt.show()