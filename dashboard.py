import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# connect database
conn = sqlite3.connect("sales.db")

# load data
df = pd.read_sql("SELECT * FROM sales", conn)

st.title("Sales Analytics Dashboard")

# -------------------
# Filters
# -------------------

countries = df["Country"].unique()
categories = df["Category"].unique()

selected_country = st.selectbox("Select Country", ["All"] + list(countries))
selected_category = st.selectbox("Select Category", ["All"] + list(categories))

filtered_df = df.copy()

if selected_country != "All":
    filtered_df = filtered_df[filtered_df["Country"] == selected_country]

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

# -------------------
# KPI Cards
# -------------------

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order_ID"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Orders", total_orders)

# -------------------
# Monthly Revenue Trend
# -------------------

monthly = filtered_df.groupby("Order_Date")["Sales"].sum().reset_index()

fig, ax = plt.subplots()

ax.plot(monthly["Order_Date"], monthly["Sales"], marker="o")

ax.set_title("Revenue Trend")

plt.xticks(rotation=45)

st.pyplot(fig)

# -------------------
# Top Products
# -------------------

top_products = (
    filtered_df.groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig2, ax2 = plt.subplots()

top_products.plot(kind="bar", ax=ax2)

ax2.set_title("Top Selling Products")

plt.xticks(rotation=45)

st.pyplot(fig2)

# -------------------
# Sales by Country
# -------------------

country_sales = filtered_df.groupby("Country")["Sales"].sum()

fig3, ax3 = plt.subplots()

country_sales.plot(kind="pie", autopct="%1.1f%%", ax=ax3)

ax3.set_ylabel("")

ax3.set_title("Sales Distribution by Country")

st.pyplot(fig3)