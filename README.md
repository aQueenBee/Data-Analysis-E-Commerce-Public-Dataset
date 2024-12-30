# Setup Environment

conda create --name dashboard
conda activate dashboard  
pip install pandas numpy matplotlib seaborn streamlit

# Run Streamlit App

streamlit run main.py

# Project:

- Import and clean customer review data.
- Visualize average product review scores.
- Analyze review score trends over time using monthly resampled data.
