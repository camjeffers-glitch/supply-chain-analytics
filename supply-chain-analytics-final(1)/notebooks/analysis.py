# analysis.py (convertible to Jupyter Notebook)

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# STEP 1: Load dataset
orders = pd.read_csv("data/sample_orders.csv")
print("First few rows of orders dataset:")
print(orders.head())

# STEP 2: Create SQL database
conn = sqlite3.connect("supply_chain.db")
orders.to_sql("orders", conn, if_exists="replace", index=False)

# STEP 3: Run SQL queries for KPIs
query = """
SELECT product_id,
       COUNT(order_id) as total_orders,
       AVG(lead_time_days) as avg_lead_time
FROM orders
GROUP BY product_id
ORDER BY total_orders DESC
"""
results = pd.read_sql(query, conn)
print("\nKPI results:")
print(results)

# STEP 4: Visualization
results.plot(x="product_id", y="avg_lead_time", kind="bar")
plt.title("Average Lead Time by Product")
plt.ylabel("Days")
plt.show()
