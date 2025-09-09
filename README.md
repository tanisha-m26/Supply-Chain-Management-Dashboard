# Supply Chain Management Dashboard

A real-time **Supply Chain Analytics Dashboard** built using **MySQL** and **Tableau**, with a structured dataset for inventory, suppliers, orders, and logistics.  
This project enables **data-driven decision-making** by visualizing KPIs such as inventory turnover, supplier performance, lead times, and demand fulfillment.

---

## 📂 Repository Structure

Supply-Chain-Management-Dashboard/
│── data/
│ ├── supply_chain.csv # Original dataset
│ ├── processed_data.xlsx # Cleaned & prepared dataset
│ ├── create_tables.sql # SQL schema (tables)
│ ├── sample_inserts.sql # Insert queries with sample records
│ └── schema.sql # Master SQL schema + constraints
│
│── sql/
│ └── queries.sql # Common SQL queries for analysis
│
│── tableau/
│ ├── SCM_Dashboard.twbx # Tableau packaged workbook
│ ├── calculated_fields.txt # Custom fields used in Tableau
│ └── screenshots/ # Dashboard visuals
│ ├── inventory_view.png
│ ├── supplier_performance.png
│ └── final_dashboard.png
│
│── docs/
│ ├── Project_Report.pdf # Final project report
│ └── Presentation.pptx # Slides for showcase
│
│── project_setup.ipynb # Notebook for preprocessing dataset
│── requirements.txt # Dependencies for preprocessing
│── README.md # Documentation
│── LICENSE # License file



---

## 🚀 Project Overview

This project demonstrates the end-to-end flow of **data ingestion, transformation, and visualization** in a supply chain domain:

1. **Database Layer (MySQL)**  
   - Schema design for suppliers, inventory, orders, logistics.  
   - Insert scripts generated from raw CSV.  
   - Analytical SQL queries (e.g., demand forecasting, supplier ranking).

2. **Data Preprocessing (Python + Pandas)**  
   - Cleaning and formatting dataset.  
   - Exporting `processed_data.xlsx` for Tableau consumption.

3. **Visualization Layer (Tableau)**  
   - Multi-tab dashboard with interactive visuals.  
   - KPIs: Inventory turnover, stock-out rate, supplier delays.  
   - Exported screenshots for documentation.

---

## 📊 Key Features

- **Inventory Analysis**: Stock levels, turnover ratio, carrying costs.  
- **Supplier Performance**: Lead times, order accuracy, cost efficiency.  
- **Order Fulfillment**: On-time delivery %, backorder tracking.  
- **Demand-Supply Balance**: Forecast vs. actual demand trends.  
- **Geographic Insights**: Supplier and warehouse locations.

---

## ⚙️ Installation & Setup

### 1️⃣ Database Setup (MySQL)
```bash
# Start MySQL server and login
mysql -u root -p

# Create database
CREATE DATABASE supply_chain;

# Import schema
SOURCE data/create_tables.sql;

# Insert data
SOURCE data/sample_inserts.sql;


2️⃣ Python Environment 

# Install dependencies
pip install -r requirements.txt

3️⃣ Tableau

Open tableau/SCM_Dashboard.twbx in Tableau Desktop.

Connect to MySQL database or use processed_data.xlsx.

📈 Example SQL Queries

Some queries available in sql/queries.sql:

Top 5 suppliers by order volume.

Monthly inventory turnover.

Average lead time per supplier.

Orders delayed beyond SLA.

🖼️ Dashboard Preview

Inventory View


Supplier Performance


Final Dashboard

📚 Documentation

Full explanation in docs/Project_Report.pdf

Presentation deck: docs/Presentation.pptx

📜 License

This project is licensed under the MIT License – see LICENSE
 file for details.


 🤝 Contributors

Your TANISHA MANGLIYA – Data Engineering & Visualization

