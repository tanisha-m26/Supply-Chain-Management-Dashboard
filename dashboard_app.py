# dashboard_app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.data_processing import run_pipeline

st.set_page_config(page_title="Supply Chain Dashboard", layout="wide")
st.title("📦 Supply Chain Management Dashboard")

# Load / process data
df = run_pipeline('data/supply_chain.csv', 'data/processed_data.xlsx')

# ---------------------------
# Sidebar filters
# ---------------------------
st.sidebar.header("Filters")
regions = st.sidebar.multiselect("Select Location", options=df['location'].unique(), default=df['location'].unique())
products = st.sidebar.multiselect("Select Product Type", options=df['product_type'].unique(), default=df['product_type'].unique())
carriers = st.sidebar.multiselect("Select Shipping Carrier", options=df['shipping_carriers'].unique(), default=df['shipping_carriers'].unique())

df_filtered = df[(df['location'].isin(regions)) & 
                 (df['product_type'].isin(products)) & 
                 (df['shipping_carriers'].isin(carriers))]

# ---------------------------
# KPI Metrics
# ---------------------------
st.subheader("Key Metrics")
total_revenue = df_filtered['total_revenue'].sum()
avg_lead_time = df_filtered['lead_time'].mean()
delayed_shipments = df_filtered['delayed_shipment'].sum()
delivery_ratio = df_filtered['delivery_ratio'].mean()
avg_inventory_turnover = df_filtered['inventory_turnover'].mean()
avg_shipping_cost = df_filtered['avg_shipping_cost'].mean()

kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)
kpi1.metric("Total Revenue ($)", f"{total_revenue:,.2f}")
kpi2.metric("Avg Lead Time (days)", f"{avg_lead_time:.2f}")
kpi3.metric("Delayed Shipments", f"{delayed_shipments}")
kpi4.metric("On-time Delivery Ratio", f"{delivery_ratio:.2%}")
kpi5.metric("Avg Inventory Turnover", f"{avg_inventory_turnover:.2f}")
kpi6.metric("Avg Shipping Cost ($/unit)", f"{avg_shipping_cost:.2f}")

# ---------------------------
# Visualizations
# ---------------------------
st.subheader("Visualizations")

# Revenue by Product Type
fig1 = px.bar(df_filtered.groupby('product_type')['total_revenue'].sum().reset_index(),
              x='product_type', y='total_revenue', title="Total Revenue by Product Type")
st.plotly_chart(fig1, use_container_width=True)

# Avg Lead Time by Location
fig2 = px.bar(df_filtered.groupby('location')['lead_time'].mean().reset_index(),
              x='location', y='lead_time', title="Average Lead Time by Location")
st.plotly_chart(fig2, use_container_width=True)

# Heatmap of Delayed Shipments by Location x Product Type
heatmap_data = df_filtered.pivot_table(index='location', columns='product_type', values='delayed_shipment', aggfunc='mean')
fig3 = px.imshow(heatmap_data, text_auto=True, color_continuous_scale='RdYlGn_r', title="Delay Heatmap (1=Delayed)")
st.plotly_chart(fig3, use_container_width=True)

# Revenue Trend over Time (if shipment_date exists)
if 'shipment_date' in df_filtered.columns:
    df_filtered['shipment_date'] = pd.to_datetime(df_filtered['shipment_date'])
    trend_data = df_filtered.groupby('shipment_date')['total_revenue'].sum().reset_index()
    fig4 = px.line(trend_data, x='shipment_date', y='total_revenue', title="Revenue Trend Over Time")
    st.plotly_chart(fig4, use_container_width=True)

# ---------------------------
# Download Processed Data
# ---------------------------
st.subheader("Download Processed Data")
st.download_button(
    label="Download Excel",
    data=open('data/processed_data.xlsx', 'rb').read(),
    file_name="processed_data.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
