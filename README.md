# 📊 Sales Analytics Dashboard

An interactive sales analytics project built with **SQL, Python, and Streamlit** that explores retail sales performance and visualizes business insights.

🔗 **Live Dashboard:**
https://sales-analytics-dashboard-gaurav.streamlit.app/

---

# Project Overview

This project simulates a small retail business dataset and demonstrates a typical **data analytics workflow**:

1. Raw CSV data ingestion
2. Data cleaning and validation
3. SQL database creation
4. Analytical queries for business insights
5. Visualization of trends
6. Interactive dashboard for exploration

The goal was to practice how analysts turn raw transactional data into **actionable insights and visual reports**.

---

# Dataset

The dataset represents retail order transactions with the following fields:

Order_ID
Order_Date
Product_Name
Category
Country
Sales
Profit
Quantity

---

# Key Questions Explored

The analysis focuses on answering practical business questions:

• Which products generate the most revenue?
• How does revenue change over time?
• Which countries contribute the most sales?
• Which categories are most profitable?
• How do sales compare with profit across product categories?

---

# Dashboard Features

The Streamlit dashboard allows users to interactively explore the dataset.

Features include:

• Country and category filters
• KPI cards for revenue, profit, and order count
• Monthly revenue trend visualization
• Top-performing products chart
• Sales distribution by country
• Profit comparison across product categories

The dashboard enables quick exploration of performance across different dimensions of the data.

---

# Tech Stack

Python
Pandas
SQLite
SQL
Matplotlib
Seaborn
Streamlit
Jupyter Notebook

---

# Project Structure

sales-data-analysis
│
├── data/
│   └── sales_data.csv

├── sql/
│   └── analysis_queries.sql

├── notebooks/
│   └── sales_analysis.ipynb

├── visuals/
│   └── exported charts

├── dashboard.py
├── create_database.py
├── sales.db
└── README.md

---

# Running the Project Locally

Clone the repository:

git clone https://github.com/wizard-dreamer/Sales-analytics-dashboard-project.git

Create a virtual environment:

python -m venv .venv
.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run the dashboard:

streamlit run dashboard.py

---

# Key Insights

Some patterns visible from the analysis:

• A small number of products generate the majority of revenue
• Sales vary across months, suggesting potential seasonal patterns
• Certain countries contribute high sales but lower profit margins
• Some categories have strong revenue but weaker profitability

These insights demonstrate how sales data can help guide **pricing strategies, marketing campaigns, and product prioritization**.

---

# Future Improvements

Possible extensions for the project:

• Add forecasting for revenue trends
• Expand dataset size for more realistic analysis
• Integrate interactive charts with Plotly
• Build a KPI-focused business dashboard layout

---

# Author

**Gaurav Singh**

Built as part of a personal data analytics learning project to practice:

SQL querying
data analysis with Python
data visualization
dashboard development
