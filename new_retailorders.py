import streamlit as st
import pandas as pd
import _mysql_connector

DB_CONFIG = {
    "host": "localhost",  # Change if your database is on a different server
    "user": "root",  # Your MySQL username
    "password": "3398",  # Your MySQL password
    "database": "retail_orders_db"  # Your MySQL database name
}

import mysql.connector
import pandas as pd
import streamlit as st

# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "3398",
    "database": "retail_orders_db"
}

# Function to Fetch Data from MySQL
def fetch_data(query):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor(dictionary=True)  
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]  

        cursor.close()  
        conn.close()  

        return pd.DataFrame(data, columns=columns)  # Returning the data as DataFrame
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()  # Returning an empty DataFrame on error

st.markdown(
    "<h1 style='text-align: center; color: red;'>RETAIL ORDER ANALYSIS</h1>", 
    unsafe_allow_html=True
)
 
        # Description
st.write('<p style="font-size:160%">You will be able to✅:</p>', unsafe_allow_html=True)
#list of features
st.write('<p style="font-size:100%">&nbsp 1. check top 10 highest revenue generating products</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 2. to see top 5 cities with the highest profit margins</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 3. find total discount given for each category</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 4. to see average sale price per product category</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 5. find region with the highest average sale price</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 6. find total profit per category</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 7. find top 3 segments with the highest quantity of orders</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 8. find average discount percentage given per region</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 9. find product category with the highest total profit</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 10. find total revenue generated per year</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 11. check top 10 best-selling products based on quantity sold</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 12. find total revenue generated per month</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 13. find total number of orders placed in each region</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 14. to see product with the highest discount given</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 15. check most popular shipping mode based on the number of orders</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 16. find total number of orders placed per year</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 17. to check top 5 states with the highest total sales</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 18. find product category with the most number of orders</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 19. to see total revenue generated from each shipping mode</p>', unsafe_allow_html=True)
st.write('<p style="font-size:100%">&nbsp; 20. find top 3 most frequently ordered products</p>', unsafe_allow_html=True)

# 1. Top 10 highest revenue-generating products
query_options = {
    "1. Top 10 Highest Revenue-Generating Products": """
    SELECT product_id, SUM(List_Price * Quantity) AS Total_Revenue 
    FROM orders 
    GROUP BY product_id 
    ORDER BY total_revenue DESC 
    LIMIT 10;
""",

# 2. Top 5 cities with the highest profit margins
"2. Top 5 Cities with the Highest Profit Margins": """

     SELECT 
    City,  
    SUM((list_price - cost_price) * Quantity) / SUM(list_price * Quantity) AS profit_margin  
FROM orders  
GROUP BY City  
ORDER BY profit_margin DESC  
LIMIT 5;

""",

# 3. Total discount given for each category
"3. Total Discount Given for Each Category": """

    SELECT category,  
    SUM(List_Price * Quantity * (`Discount Percent` / 100)) AS Total_Discount  
    FROM orders 
    GROUP BY category
    ORDER BY Total_Discount DESC;

""",

# 4. Average sale price per product category
"4. Average Sale Price Per Product Category":"""
    SELECT category, AVG(List_Price) AS Average_Sale_Price  
    FROM orders 
    GROUP BY category
    ORDER BY Average_Sale_Price DESC;

""",

# 5. Region with the highest average sale price
"5. Region with the Highest Average Sale Price":"""
    SELECT region, AVG(List_Price) AS avg_sale_price 
    FROM orders 
    GROUP BY region 
    ORDER BY avg_sale_price DESC 
    LIMIT 1;

""",

# 6. Total profit per category
"6. Total Profit Per Category":"""
    SELECT category, SUM(List_Price * Quantity * (1 - `Discount Percent` / 100) - Cost_Price * Quantity) AS Total_Profit
    FROM orders 
    GROUP BY category;

""",

# 7. Top 3 segments with the highest quantity of orders
"7. Top 3 Segments with the Highest Quantity of Orders":"""
    SELECT segment, SUM(quantity) AS total_quantity 
    FROM orders 
    GROUP BY segment 
    ORDER BY total_quantity DESC 
    LIMIT 3;

""",

# 8. Average discount percentage per region
"8. Average Discount Percentage Given Per Region":"""
 
    SELECT region, AVG(`Discount Percent`) AS avg_discount 
    FROM orders 
    GROUP BY region;

""",

# 9. Product category with the highest total profit
"9. Product Category with the Highest Total Profit":"""

    SELECT category, SUM(List_Price * Quantity * (1 - `Discount Percent` / 100) - Cost_Price * Quantity) AS Total_Profit
    FROM orders 
    GROUP BY category 
    ORDER BY total_profit DESC 
    LIMIT 1;

""",

# 10. Total revenue generated per year
"10. Total Revenue Generated Per Year":"""
    SELECT YEAR('Order Date') AS year, 
    SUM(List_Price * Quantity * (1 - `Discount Percent` / 100)) AS Total_Revenue  
    FROM orders 
    GROUP BY year;

""",

# 11. Top 10 best-selling products based on quantity sold
"11. Top 10 Best-Selling Products Based on Quantity Sold":"""
    SELECT product_id, SUM(Quantity) AS Total_Quantity_Sold 
    FROM orders 
    GROUP BY product_id 
    ORDER BY Total_Quantity_Sold DESC 
    LIMIT 10;

""",

# 12. Total revenue generated per month
"12. Total Revenue Generated Per Month":"""
    SELECT  
    YEAR(`Order Date`) AS Year,  
    MONTH(`Order Date`) AS Month,  
    SUM(List_Price * Quantity * (1 - `Discount Percent` / 100)) AS Total_Revenue  
FROM orders  
GROUP BY Year, Month  
ORDER BY Year, Month;

""",

# 13. Total number of orders placed in each region
"13. Total Number of Orders Placed in Each Region":"""
    SELECT region, COUNT('Order Id') AS total_orders 
    FROM orders 
    GROUP BY region;
    ORDER BY Total_Orders DESC;

""",

# 14. Product with the highest discount given
"14. Product with the Highest Discount Given":"""
    SELECT product_id, MAX('discount percent') AS highest_discount 
    FROM orders 
    GROUP BY product_id 
    ORDER BY highest_discount DESC 
    LIMIT 1;

""",

# 15. Most popular shipping mode based on the number of orders
"15. Most Popular Shipping Mode Based on Orders":"""
    SELECT 'Ship Mode', COUNT('Order Id') AS total_orders 
    FROM orders 
    GROUP BY 'Ship Mode'
    ORDER BY total_orders DESC 
    LIMIT 1;

""",

# 16. Total number of orders placed per year
"16. Total Number of Orders Placed Per Year":"""
    SELECT  
    YEAR(`Order Date`) AS Year,  
    COUNT(`Order ID`) AS Total_Orders  
FROM orders  
GROUP BY YEAR(`Order Date`)  
ORDER BY Year ASC;

""",

# 17. Top 5 states with the highest total sales
"17. Top 5 States with the Highest Total Sales":"""
    SELECT `State`,  
    SUM(List_Price * Quantity * (1 - `Discount Percent` / 100)) AS Total_Sales  
FROM orders  
GROUP BY `State`  
ORDER BY Total_Sales DESC  
LIMIT 5;

""",

# 18. Product category with the most number of orders
"18. Product Category with the Most Number of Orders":"""
    SELECT `Category`, COUNT(`Order ID`) AS Total_Orders  
FROM orders  
GROUP BY `Category`  
ORDER BY Total_Orders DESC  
LIMIT 1;

""",

# 19. Total revenue generated from each shipping mode
"19. Total Revenue Generated from Each Shipping Mode":"""
    SELECT`Ship Mode`,  
    SUM(List_Price * Quantity * (1 - `Discount Percent` / 100)) AS Total_Revenue  
FROM orders  
GROUP BY `Ship Mode`  
ORDER BY Total_Revenue DESC;

""",

# 20. Top 3 most frequently ordered products
"20. Top 3 Most Frequently Ordered Products":"""
    SELECT product_id, COUNT(`Order ID`) AS order_count 
    FROM orders 
    GROUP BY product_id 
    ORDER BY order_count DESC 
    LIMIT 3;
"""
}

# ✅ Sidebar: Multi-select dropdown with "Select All" feature
query_list = list(query_options.keys())  # Get all query keys
selected_queries = st.sidebar.multiselect("Select Queries:", ["Select All"] + query_list, default=["Select All"])

# ✅ Handle "Select All" case
if "Select All" in selected_queries:
    selected_queries = query_list  # Show all queries

# ✅ Define `show_full_results` checkbox
show_full_results = st.sidebar.checkbox("Show Full Results", value=False)

# ✅ Execute each selected query and display results
for query in selected_queries:
    df = fetch_data(query_options[query])  # Ensure `fetch_data()` is defined

    if df is not None and not df.empty:
        if "Year" in df.columns:
            df["Year"] = df["Year"].astype(str)

        # ✅ Limit rows if "Show Full Results" is not checked
        if not show_full_results:
            df = df.head(10)

        st.write(f"### Results for: {query}")
        st.dataframe(df)
    else:
        st.warning(f"No data found for: {query}")