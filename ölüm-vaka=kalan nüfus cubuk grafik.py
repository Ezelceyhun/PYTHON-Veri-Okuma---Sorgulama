import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("coronavirus.csv")
sutun1 = data.iloc[0:, 3]
sutun2 = data.iloc[0:, 5]
sutun3 = data.iloc[0:, 6]
sonuc_ek = sutun2 + sutun3
sonuc = sutun1 - sonuc_ek
data = data.sort_values(by="Continent")
plt.figure(figsize=(16 , 13))
plt.bar(data["Continent"],sonuc, color='blue', width=0.9)
plt.xlabel('Kıtalar', fontsize=30)
plt.ylabel('Nüfus(milyon ile ifade edilir)', fontsize=30)
plt.title('Vaka ve Ölümler Çıkarıldıktan Sonra Kalan Sağlıklı Toplam Nüfus', fontsize=30)
plt.show()