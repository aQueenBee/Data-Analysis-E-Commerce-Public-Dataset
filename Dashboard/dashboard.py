import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load datasets
@st.cache_resource
def load_data():
    # Load order items dataset
    url_order_items = "https://raw.githubusercontent.com/aQueenBee/Data-Analysis-E-Commerce-Public-Dataset/Data-Analysis-E-Commerce-Public-Dataset/data/order_items_dataset.csv"
    order_items = pd.read_csv(url_order_items)

    # Load order reviews dataset
    url_order_reviews = "https://raw.githubusercontent.com/aQueenBee/Data-Analysis-E-Commerce-Public-Dataset/Data-Analysis-E-Commerce-Public-Dataset/data/order_reviews_dataset.csv"
    order_reviews = pd.read_csv(url_order_reviews)

    return order_items.copy(), order_reviews.copy()

order_items, order_reviews = load_data()

# Display datasets
st.subheader("Order Items Dataset:")
st.write(order_items.head())

st.subheader("Order Reviews Dataset:")
st.write(order_reviews.head())

# Descriptive Statistics
st.subheader("Descriptive Statistics - Order Items Dataset:")
st.write(order_items.describe())

st.subheader("Descriptive Statistics - Order Reviews Dataset:")
st.write(order_reviews.describe())

# Merge datasets and analyze
merged_data = pd.merge(order_items[['order_id', 'product_id']],
                       order_reviews[['order_id', 'review_score']],
                       on='order_id',
                       how='inner')

average_scores_per_product = merged_data.groupby('product_id')['review_score'].mean().reset_index()

# Display average scores per product
st.subheader("Average Review Scores per Product:")
st.write(average_scores_per_product.head())

# Plot bar plot for sampled products
sampled_products = average_scores_per_product.sample(n=100, random_state=42)

plt.figure(figsize=(12, 6))
plt.bar(range(len(sampled_products)), sampled_products['review_score'], color='skyblue')
plt.xlabel('Product')  
plt.ylabel('Average Review Score')
plt.title('Average Review Score for 100 Sampled Products')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
st.pyplot(plt)

# Analyze trend over time
order_reviews['review_creation_date'] = pd.to_datetime(order_reviews['review_creation_date'])
order_reviews['year'] = order_reviews['review_creation_date'].dt.year

average_scores_time = order_reviews.groupby('year')['review_score'].mean().reset_index()

# Display trend over time
st.subheader("Average Review Scores Over Time:")
st.write(average_scores_time)

# Plot trend over time
plt.figure(figsize=(10, 6))
plt.plot(average_scores_time['year'], average_scores_time['review_score'], marker='o', color='b')
plt.title('Review Score Trend Over Time')
plt.xlabel('Year')
plt.ylabel('Average Review Score')
plt.grid(True)
st.pyplot(plt)