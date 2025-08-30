-- Total orders by product
SELECT product_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY product_id;

-- Average lead time
SELECT AVG(lead_time_days) AS avg_lead_time
FROM orders;

-- Fill rate (fulfilled / total)
SELECT product_id,
       SUM(CASE WHEN fulfilled = 1 THEN 1 ELSE 0 END) * 1.0 / COUNT(order_id) AS fill_rate
FROM orders
GROUP BY product_id;
