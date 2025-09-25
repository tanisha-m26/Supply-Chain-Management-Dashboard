# scripts/data_processing.py
import pandas as pd
import numpy as np

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    # Rename columns to snake_case if needed
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

    # Handle missing values
    df.fillna({
        'price': 0,
        'availability': 0,
        'number_of_products_sold': 0,
        'revenue_generated': 0,
        'stock_levels': 0,
        'lead_times': df['lead_times'].median() if 'lead_times' in df.columns else 0,
        'shipping_costs': 0,
        'manufacturing_costs': 0,
        'defect_rates': 0
    }, inplace=True)

    return df

def add_calculated_fields(df):
    # Total revenue = revenue_generated
    df['total_revenue'] = df['revenue_generated']

    # Delayed shipments (lead_time > 7 days)
    df['delayed_shipment'] = np.where(df['lead_time'] > 7, 1, 0)

    # On-time delivery ratio by region/location
    df['delivery_ratio'] = df.groupby('location')['delayed_shipment'].transform(lambda x: 1 - x.mean())

    # Inventory turnover = number_of_products_sold / average stock
    df['inventory_turnover'] = df['number_of_products_sold'] / df.groupby('sku')['stock_levels'].transform('mean')

    # Average shipping cost per unit
    df['avg_shipping_cost'] = df['shipping_costs'] / df['order_quantities']

    return df

def save_processed_data(df, output_path):
    df.to_excel(output_path, index=False)
    print(f"Processed data saved to {output_path}")

def run_pipeline(input_csv, output_excel):
    df = load_data(input_csv)
    df = clean_data(df)
    df = add_calculated_fields(df)
    save_processed_data(df, output_excel)
    return df

if __name__ == "__main__":
    run_pipeline('data/supply_chain.csv', 'data/processed_data.xlsx')
