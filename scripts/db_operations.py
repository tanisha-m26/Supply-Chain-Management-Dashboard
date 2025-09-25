# scripts/db_operations.py
import sqlite3
import pandas as pd

DB_FILE = 'data/supply_chain.db'  # SQLite database file

def create_connection(db_file=DB_FILE):
    """Create a database connection to SQLite."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except Exception as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_table(conn):
    """Create table if it doesn't exist."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS supply_chain (
        product_type TEXT,
        sku TEXT PRIMARY KEY,
        price REAL,
        availability INTEGER,
        number_of_products_sold INTEGER,
        revenue_generated REAL,
        customer_demographics TEXT,
        stock_levels INTEGER,
        lead_times INTEGER,
        order_quantities INTEGER,
        shipping_times INTEGER,
        shipping_carriers TEXT,
        shipping_costs REAL,
        supplier_name TEXT,
        location TEXT,
        lead_time INTEGER,
        production_volumes INTEGER,
        manufacturing_lead_time INTEGER,
        manufacturing_costs REAL,
        inspection_results TEXT,
        defect_rates REAL,
        transportation_modes TEXT,
        routes TEXT,
        costs REAL,
        total_revenue REAL,
        delayed_shipment INTEGER,
        delivery_ratio REAL,
        inventory_turnover REAL,
        avg_shipping_cost REAL
    );
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
        print("Table 'supply_chain' created successfully (if not exists).")
    except Exception as e:
        print(f"Error creating table: {e}")

def insert_data(conn, df):
    """Insert data from processed DataFrame into the database."""
    try:
        df.to_sql('supply_chain', conn, if_exists='replace', index=False)
        print(f"Inserted {len(df)} rows into 'supply_chain' table.")
    except Exception as e:
        print(f"Error inserting data: {e}")

def run_queries(conn, queries_file):
    """Run SQL queries from a file (for Tableau or reports)."""
    try:
        with open(queries_file, 'r') as f:
            queries = f.read().split(';')
        c = conn.cursor()
        for query in queries:
            query = query.strip()
            if query:
                c.execute(query)
        conn.commit()
        print("Queries executed successfully.")
    except Exception as e:
        print(f"Error running queries: {e}")

def main():
    import os
    processed_file = 'data/processed_data.xlsx'
    
    if not os.path.exists(processed_file):
        print("Processed data not found. Run data_processing.py first.")
        return
    
    # Load processed data
    df = pd.read_excel(processed_file)
    
    # Connect to database
    conn = create_connection()
    if conn:
        # Create table
        create_table(conn)
        
        # Insert data
        insert_data(conn, df)
        
        # Optional: run queries from file
        queries_file = 'sql/queries.sql'
        if os.path.exists(queries_file):
            run_queries(conn, queries_file)
        
        conn.close()
        print("Database operations completed.")

if __name__ == "__main__":
    main()
