# Sales Data Analytics using SQL & Python

## Overview

This project explores a simulated retail sales dataset and demonstrates a complete analytics workflow — from raw data ingestion to insight generation.

The goal was to practice how analysts typically work with business data: clean the dataset, structure it in a database, run analytical SQL queries, and visualize trends that help explain business performance.

The dataset includes the following fields:

Order_ID, Order_Date, Product_Name, Category, Country, Sales, Profit, Quantity

---

## Project Structure

data/
  sales_data.csv – raw dataset

sql/
  analysis_queries.sql – analytical SQL queries

notebooks/
  sales_analysis.ipynb – exploration and visualization

visuals/
  exported charts generated during analysis

create_database.py
  script that cleans the data and builds the SQLite database

README.md
  project documentation

---

## Tools Used

Python
Pandas
SQLite
Matplotlib
Seaborn
Jupyter Notebook
SQL

---

## Data Preparation

Before performing analysis, the dataset is cleaned and validated using `create_database.py`.

Key preparation steps include:

• removing empty rows
• validating required columns
• converting numeric fields (Sales, Profit, Quantity)
• removing duplicates
• filtering unrealistic values (negative sales or zero quantities)
• creating a helper summary table for quick aggregations

This ensures the analysis is based on consistent and reliable data.

---

## Analysis Performed

The project answers several basic business questions:

• Which products generate the most revenue?
• How do sales and profits change over time?
• Which countries contribute the most to total sales?
• Which product categories are the most profitable?
• How do category sales compare to profit margins?

These questions are explored using SQL queries and Python-based visualizations.

---

## Visualizations

The notebook generates and exports several charts, including:

• Top selling products
• Monthly revenue and profit trends
• Sales distribution by country
• Profit by product category
• Category sales vs profit relationship
• Monthly sales trends across categories

All generated charts are saved in the `visuals/` folder.

---

## Key Observations

Some interesting patterns visible in the dataset:

• A small number of products contribute disproportionately to revenue
• Sales fluctuate month-to-month, suggesting possible seasonal demand
• Certain countries generate strong revenue but lower profit margins
• Some categories show high sales but relatively weaker profitability

These types of insights help businesses decide where to focus growth or optimization efforts.

---

## Running the Project

Create a virtual environment (recommended):

python -m venv .venv
.venv\Scripts\activate

Install required packages:

pip install pandas matplotlib seaborn jupyter

Generate the SQLite database:

python create_database.py

Launch the notebook:

cd notebooks
jupyter notebook sales_analysis.ipynb

Run the notebook cells to reproduce the analysis and charts.

---

## Possible Improvements

Some future extensions for this project:

• build an interactive dashboard using Streamlit
• expand the dataset to simulate larger sales volumes
• include forecasting for future revenue trends
• add KPI dashboards for business reporting

---

## Purpose of the Project

This project was built as a practice exercise to strengthen core data analytics skills including:

SQL querying
data cleaning
data visualization
business insight extraction

It represents a small but complete analytics workflow that could be extended into a full dashboard or reporting system.
