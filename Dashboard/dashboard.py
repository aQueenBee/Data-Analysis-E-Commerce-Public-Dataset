import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#Raw URL of the CSV file on GitHub
csv_url = 'https://raw.githubusercontent.com/aQueenBee/Data-Analysis-E-Commerce-Public-Dataset/Data-Analysis-E-Commerce-Public-Dataset/Dashboard/main_data.csv'
#Read the CSV file into a Pandas DataFrame
data = pd.read_csv(csv_url)
#Display the first few rows of the DataFrame
print(data.head())

# Hitung rata-rata skor ulasan
mean_review_score = data['review_score'].mean()

# Tampilkan judul aplikasi
st.title('Distribution of Review Scores')

# Tampilkan histogram menggunakan Seaborn tanpa KDE dan garis tepi
plt.figure(figsize=(8, 6))
sns.histplot(data['review_score'], bins=5, kde=False, color='skyblue')
plt.axvline(mean_review_score, color='red', linestyle='dashed', linewidth=1, label=f'Mean Score: {mean_review_score:.2f}')
plt.title('Distribution of Review Scores')
plt.xlabel('Review Score')
plt.ylabel('Frequency')
plt.legend()
plt.grid(True)
st.pyplot(plt)

# Tampilkan rata-rata skor ulasan
st.write(f"Mean Review Score: {mean_review_score:.2f}")



# Convert 'review_creation_date' to datetime format
data['review_creation_date'] = pd.to_datetime(data['review_creation_date'])

# Extract year from 'review_creation_date'
data['year'] = data['review_creation_date'].dt.year

# Count the number of reviews for each year
review_count_by_year = data['year'].value_counts().sort_index()

# Calculate the percentage change in review count from the previous year
review_count_change = review_count_by_year.pct_change().fillna(0) * 100

# Display the title for the Streamlit app
st.title('Review Count and Percentage Change by Year')

# Create the plot using seaborn line plot with markers
plt.figure(figsize=(10, 6))

# Plot the review count by year
sns.lineplot(x=review_count_by_year.index, y=review_count_by_year.values, marker='o', color='skyblue', label='Review Count')

# Plot the percentage change from the previous year
sns.lineplot(x=review_count_change.index, y=review_count_change.values, marker='o', color='red', label='Percentage Change (%)')

# Annotate the points with count and percentage change values
for i, count in enumerate(review_count_by_year.values):
    plt.text(review_count_by_year.index[i], count, f'{count}', ha='right', va='bottom', color='black')
    plt.text(review_count_change.index[i], review_count_change.values[i], f'{review_count_change.values[i]:.2f}%', ha='right', va='bottom', color='black')

plt.xlabel('Year')
plt.ylabel('Count / Percentage Change')
plt.title('Review Count and Percentage Change by Year')
plt.xticks(rotation=45)
plt.legend()


# Display the plot
st.pyplot(plt)