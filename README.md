# Supply Chain Analytics Project

I created this project to practice using **Python** and **SQL** in the context of supply chain problems. The idea is to take a dataset that looks like real client data (orders, lead times, fulfillment status) and turn it into insights a consultant might deliver. 

---

## Why I Built This
I’m interested in supply chain consulting, and I wanted a hands-on way to show I can connect technical tools with business impact. This project is a starting point for analyzing supply chain KPIs and building a foundation for client-ready dashboards.

---

## What’s Inside
- **data/** → `sample_orders.csv` (mock dataset of 200 orders, 5 products, lead times, fulfillment status)  
- **sql/** → basic SQL queries for KPIs like average lead time and fill rate  
- **notebooks/** → a Jupyter Notebook that loads the data, runs SQL queries, and visualizes the results  
- **app.py** → placeholder for a Streamlit dashboard I plan to build later  

---

## Current Progress
- Loaded dataset into a SQL database  
- Built queries for key KPIs  
- Created first visualizations in Python  
- Next step: interactive dashboard for client-style presentations  

---

## Example Output
The notebook currently shows:
- Average lead time per product (visualized in a bar chart)  
- Order volumes by product  
- Fulfillment performance  

---

## Tools I’m Using
- **Python (Pandas, Matplotlib)** for analysis and visualization  
- **SQL (SQLite)** for queries  
- **Streamlit** (planned) for dashboards  

---

## Next Steps
I want to:
1. Add more KPIs (inventory turnover, cost per order).  
2. Build the Streamlit app so results are interactive.  
3. Expand the dataset to mimic a larger supply chain (warehouses, suppliers, etc.).  

---

## License
MIT License — open to share and learn from.  
