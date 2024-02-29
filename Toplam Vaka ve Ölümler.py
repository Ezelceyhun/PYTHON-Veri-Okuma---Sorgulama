import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("coronavirus.csv")
top_vaka = data["Total Cases"]
plt.subplot(1,2,1)
plt.plot(top_vaka)
plt.title("Toplam Vakalar")
top_olum = data["Total Deaths"]
plt.subplot(1,2,2)
plt.plot(top_olum)
plt.title("Toplam Ölümler")
plt.show()