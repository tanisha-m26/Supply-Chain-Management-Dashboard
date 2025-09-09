-- queries.sql

-- Inventory Management
SELECT product_type, sku, stock_levels, availability
FROM supply_chain;

SELECT product_type, SUM(stock_levels) AS total_stock
FROM supply_chain
GROUP BY product_type;

-- Days of Inventory Remaining (needs avg daily sales, approximated here)
SELECT sku, stock_levels / NULLIF(AVG(number_of_products_sold), 0) AS days_inventory_remaining
FROM supply_chain
GROUP BY sku, stock_levels;

-- Order Fulfillment
SELECT COUNT(sku) AS total_orders,
       SUM(CASE WHEN shipping_times <= lead_times THEN 1 ELSE 0 END) AS on_time_orders,
       SUM(CASE WHEN shipping_times <= lead_times THEN 1 ELSE 0 END) / COUNT(sku) * 100 AS on_time_delivery_rate
FROM supply_chain;

-- Supplier Performance
SELECT supplier_name, AVG(lead_time) AS avg_delivery_time, AVG(defect_rates) AS avg_defect_rate
FROM supply_chain
GROUP BY supplier_name;

-- Transportation Efficiency
SELECT shipping_carriers, AVG(shipping_times) AS avg_transit_time
FROM supply_chain
GROUP BY shipping_carriers;

-- Supply Chain Costs
SELECT transportation_modes, SUM(costs) AS total_cost
FROM supply_chain
GROUP BY transportation_modes;

SELECT SUM(costs) AS overall_costs FROM supply_chain;
