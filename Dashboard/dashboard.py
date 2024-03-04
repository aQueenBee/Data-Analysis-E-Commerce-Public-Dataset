import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sea

data = pd.read_csv('Dashboard/main_data.csv')
print(data.head())

#Melihat dimensi data
print("Jumlah baris dan kolom:", data.shape)

#Melihat tipe data dari setiap kolom
print(data.dtypes)

#Memeriksa nilai yang hilang atau tidak valid
print(data.isnull().sum())

#Memilih kolom yang diperlukan
data_selected = data[['review_score', 'review_creation_date']]

#Menampilkan lima baris pertama dari data/kolom yang dipilih
print(data_selected.head())

#Melihat dimensi data
print("Jumlah baris dan kolom sebelum cleansing:", data.shape)

#Melihat tipe data dari setiap kolom
print("\nTipe data dari setiap kolom sebelum cleansing:")
print(data.dtypes)

#Memeriksa nilai yang hilang atau tidak valid
print("\nJumlah nilai yang hilang atau tidak valid sebelum cleansing:")
print(data.isnull().sum())

#Memilih hanya kolom yang diperlukan
data_selected = data[['review_score', 'review_creation_date']]

#Menampilkan lima baris pertama dari data yang dipilih sebelum cleansing
print("\nLima baris pertama dari data yang dipilih sebelum cleansing:")
print(data_selected.head())

#Menghapus baris dengan nilai yang hilang
data_cleaned = data_selected.dropna()

#Menampilkan dimensi data setelah cleansing
print("\nJumlah baris dan kolom setelah cleansing:", data_cleaned.shape)

#Menampilkan lima baris pertama dari data yang dipilih setelah cleansing
print("\nLima baris pertama dari data yang dipilih setelah cleansing:")
print(data_cleaned.head())

#Menampilkan statistik deskriptif untuk data yang telah dibersihkan
print("Statistik Deskriptif untuk review_score:")
print(data_cleaned['review_score'].describe())

#Mengonversi kolom review_creation_date menjadi tipe data datetime
data_cleaned['review_creation_date'] = pd.to_datetime(data_cleaned['review_creation_date'])

#Menampilkan statistik deskriptif untuk kolom review_creation_date
print("\nStatistik Deskriptif untuk review_creation_date:")
print(data_cleaned['review_creation_date'].describe())

#Mengonversi kolom review_creation_date menjadi tipe data datetime
data_cleaned['review_creation_date'] = pd.to_datetime(data_cleaned['review_creation_date'])

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
monthly_average = data_cleaned.resample('M').mean()

plt.figure(figsize=(10, 6))
plt.plot(monthly_average.index, monthly_average['review_score'], marker='o', linestyle='-', color='skyblue')
plt.title('Tren Skor Ulasan dari Waktu ke Waktu')
plt.xlabel('Tanggal Pembuatan Ulasan')
plt.ylabel('Skor Rata-rata Ulasan Bulanan')
plt.ylim(0, 5)  # Memastikan batas y mulai dari 0 hingga 5
plt.xticks(rotation=45)  # Putar label sumbu x agar lebih mudah dibaca
plt.grid(True)
plt.show()
