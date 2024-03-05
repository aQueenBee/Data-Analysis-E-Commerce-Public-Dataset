import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Unduh data CSV dari URL
url_order_items = "https://raw.githubusercontent.com/aQueenBee/Data-Analysis-E-Commerce-Public-Dataset/Data-Analysis-E-Commerce-Public-Dataset/data/order_items_dataset.csv"
order_items = pd.read_csv(url_order_items)
# URL dataset order reviews
url_order_reviews = "https://raw.githubusercontent.com/aQueenBee/Data-Analysis-E-Commerce-Public-Dataset/Data-Analysis-E-Commerce-Public-Dataset/data/order_reviews_dataset.csv"
order_reviews = pd.read_csv(url_order_reviews)

# Ambil 100 sampel produk secara acak
sampled_products = average_scores_per_product.sample(n=100, random_state=42)

# Plot bar plot dari sampel data
plt.figure(figsize=(12, 6))
plt.bar(range(len(sampled_products)), sampled_products['review_score'], color='skyblue')
plt.xlabel('Produk')  # Memberikan label kosong pada sumbu x
plt.ylabel('Rata-rata Skor Ulasan')
plt.title('Rata-rata Skor Ulasan untuk 100 Sampel Produk')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Visualisasikan tren skor ulasan dari waktu ke waktu menggunakan line chart
plt.figure(figsize=(10, 6))
plt.plot(average_scores_time['year'], average_scores_time['review_score'], marker='o', color='b')
plt.title('Tren Skor Ulasan dari Waktu ke Waktu')
plt.xlabel('Tahun')
plt.ylabel('Rata-rata Skor Ulasan')
plt.grid(True)
plt.show()