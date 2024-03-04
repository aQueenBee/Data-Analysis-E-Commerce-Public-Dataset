import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea


#Visualisasi rata-rata skor ulasan
average_score = data_cleaned['review_score'].mean()

plt.figure(figsize=(8, 6))
plt.bar(['Rata-rata Skor Ulasan'], [average_score], color='skyblue')
plt.title('Rata-rata Skor Ulasan dari Seluruh Pesanan')
plt.ylabel('Skor Rata-rata')
plt.ylim(0, 5)  #Memastikan batas y mulai dari 0 hingga 5
plt.text(0, average_score, f'{average_score:.2f}', ha='center', va='bottom', fontsize=12)
plt.show()

#Visualisasi tren skor ulasan dari waktu ke waktu
data_cleaned.set_index('review_creation_date', inplace=True)
monthly_average = data_cleaned.resample('ME').mean()

plt.figure(figsize=(10, 6))
plt.plot(monthly_average.index, monthly_average['review_score'], marker='o', linestyle='-', color='skyblue')
plt.title('Tren Skor Ulasan dari Waktu ke Waktu')
plt.xlabel('Tanggal Pembuatan Ulasan')
plt.ylabel('Skor Rata-rata Ulasan Bulanan')
plt.ylim(0, 5)  # Memastikan batas y mulai dari 0 hingga 5
plt.xticks(rotation=45)  # Putar label sumbu x agar lebih mudah dibaca
plt.grid(True)
plt.show()
