-- 1. Top 10 selling products by total quantity sold
SELECT Product_Name,
       Category,
       SUM(Quantity) AS total_quantity,
       SUM(Sales) AS total_sales,
       SUM(Profit) AS total_profit
FROM sales
GROUP BY Product_Name, Category
ORDER BY total_quantity DESC
LIMIT 10;

-- 2. Monthly revenue trend (using YYYY-MM format)
SELECT strftime('%Y-%m', Order_Date) AS month,
       SUM(Sales) AS monthly_revenue,
       SUM(Profit) AS monthly_profit,
       COUNT(DISTINCT Order_ID) AS order_count
FROM sales
GROUP BY month
ORDER BY month;

-- 3. Country-wise sales performance
SELECT Country,
       SUM(Sales) AS total_sales,
       SUM(Profit) AS total_profit,
       SUM(Quantity) AS total_quantity
FROM sales
GROUP BY Country
ORDER BY total_sales DESC;

-- 4. Profit by category
SELECT Category,
       SUM(Profit) AS total_profit,
       SUM(Sales) AS total_sales,
       ROUND(SUM(Profit) * 1.0 / NULLIF(SUM(Sales), 0), 4) AS profit_margin
FROM sales
GROUP BY Category
ORDER BY total_profit DESC;

-- 5. Additional insight: Average order value and average margin by category
SELECT Category,
       ROUND(AVG(Sales / NULLIF(Quantity, 0)), 2) AS avg_price_per_unit,
       ROUND(AVG(Profit / NULLIF(Sales, 1)), 4) AS avg_margin_ratio
FROM sales
GROUP BY Category
ORDER BY avg_margin_ratio DESC;

-- 6. Additional insight: Top countries by profit margin
SELECT Country,
       SUM(Sales) AS total_sales,
       SUM(Profit) AS total_profit,
       ROUND(SUM(Profit) * 1.0 / NULLIF(SUM(Sales), 0), 4) AS margin_ratio
FROM sales
GROUP BY Country
ORDER BY margin_ratio DESC;

