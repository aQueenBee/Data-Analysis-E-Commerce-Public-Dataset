import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# URL dataset
url_main_data = "https://raw.githubusercontent.com/aQueenBee/Data-Analysis-E-Commerce-Public-Dataset/Data-Analysis-E-Commerce-Public-Dataset/Dashboard/main_data.csv"
order_items = pd.read_csv(url_main_data)

# Mengambil 100 sampel produk secara acak
sampled_products = average_scores_per_product.sample(n=100, random_state=42)

# Plot bar plot dari sampel data tanpa label indeks produk
plt.figure(figsize=(12, 6))
plt.bar(range(len(sampled_products)), sampled_products.values, color='skyblue')
plt.xlabel('Produk')  # Memberikan label kosong pada sumbu x
plt.ylabel('Rata-rata Skor Ulasan')
plt.title('Rata-rata Skor Ulasan untuk 100 Produk Pertama (Sampel)')
plt.xticks([])  # Menghapus label sumbu x
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot()

# Ambil 100 sampel produk secara acak
sampled_products = average_scores_per_product.sample(n=100, random_state=42)

# Plot grafik garis untuk setiap sampel produk
plt.figure(figsize=(12, 6))
for product_id in sampled_products.index:
    # Kelompokkan data berdasarkan tahun dan produk
    average_scores_time = merged_data[merged_data['product_id'] == product_id].groupby(merged_data['review_creation_date'].dt.year)['review_score'].mean()
    plt.plot(average_scores_time.index, average_scores_time.values, marker='o', label=None)  # Label=None untuk menonaktifkan label produk

plt.xlabel('Tahun')
plt.ylabel('Rata-rata Skor Ulasan')
plt.title('Tren Skor Ulasan dari Tahun ke Tahun (100 Sampel Produk)')
plt.grid(True)
plt.tight_layout()
st.pyplot()
