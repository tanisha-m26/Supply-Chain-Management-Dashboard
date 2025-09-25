-- Auto-generated schema
-- Removed CREATE DATABASE and USE statements for Oracle compatibility

DROP TABLE IF EXISTS supply_chain;
CREATE TABLE supply_chain (
    product_type VARCHAR(100),
    sku VARCHAR(50) PRIMARY KEY,
    price DECIMAL(10,2),
    availability INT,
    number_of_products_sold INT,
    revenue_generated DECIMAL(15,2),
    customer_demographics VARCHAR(100),
    stock_levels INT,
    lead_times INT,
    order_quantities INT,
    shipping_times INT,
    shipping_carriers VARCHAR(100),
    shipping_costs DECIMAL(10,2),
    supplier_name VARCHAR(100),
    location VARCHAR(100),
    lead_time INT,
    production_volumes INT,
    manufacturing_lead_time INT,
    manufacturing_costs DECIMAL(15,2),
    inspection_results VARCHAR(50),
    defect_rates DECIMAL(10,4),
    transportation_modes VARCHAR(50),
    routes VARCHAR(50),
    costs DECIMAL(15,2)
);
