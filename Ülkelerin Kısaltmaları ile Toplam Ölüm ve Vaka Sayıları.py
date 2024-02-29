import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("coronavirus.csv")
sutun1= data["ISO 3166-1 alpha-3 CODE"][:7]
sutun2=data["Total Cases"][:7]
sutun3=data["Total Deaths"][:7]
plt.plot(sutun1,sutun2,sutun3)
plt.title("Ülkelerin Kısaltmaları ile Toplam Ölüm ve Vaka Sayıları")
plt.show()
