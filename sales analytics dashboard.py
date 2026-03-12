import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title=Sales Analytics Dashboard, layout=wide)

st.title(📊 Sales Analytics Dashboard)

# Upload dataset
uploaded_file = st.file_uploader(Upload Sales Dataset (CSV), type=[csv])

if uploaded_file
    
    df = pd.read_csv(uploaded_file)

    st.subheader(Dataset Preview)
    st.dataframe(df.head())

    # Convert date column
    if Order_Date in df.columns
        df[Order_Date] = pd.to_datetime(df[Order_Date])
        df[Month] = df[Order_Date].dt.to_period(M).astype(str)

    # KPIs
    total_sales = df[Sales].sum()
    total_profit = df[Profit].sum()
    total_orders = df[Order_ID].nunique()
    avg_order_value = total_sales  total_orders

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(Total Sales, f${total_sales,.0f})
    col2.metric(Total Profit, f${total_profit,.0f})
    col3.metric(Total Orders, total_orders)
    col4.metric(Avg Order Value, f${avg_order_value,.2f})

    st.divider()

    # Monthly Sales Trend
    st.subheader(Monthly Sales Trend)

    monthly_sales = df.groupby(Month)[Sales].sum().reset_index()

    fig1 = px.line(monthly_sales, x=Month, y=Sales, title=Monthly Revenue)
    st.plotly_chart(fig1, use_container_width=True)

    # Sales by Region
    if Region in df.columns
        st.subheader(Sales by Region)

        region_sales = df.groupby(Region)[Sales].sum().reset_index()

        fig2 = px.bar(region_sales, x=Region, y=Sales, title=Sales by Region)
        st.plotly_chart(fig2, use_container_width=True)

    # Top Products
    if Product_Name in df.columns
        st.subheader(Top Selling Products)

        product_sales = df.groupby(Product_Name)[Sales].sum().reset_index()
        product_sales = product_sales.sort_values(by=Sales, ascending=False).head(10)

        fig3 = px.bar(product_sales, x=Product_Name, y=Sales, title=Top 10 Products)
        st.plotly_chart(fig3, use_container_width=True)

    # Sales by Category
    if Product_Category in df.columns
        st.subheader(Sales by Category)

        category_sales = df.groupby(Product_Category)[Sales].sum().reset_index()

        fig4 = px.pie(category_sales, names=Product_Category, values=Sales, title=Sales by Category)
        st.plotly_chart(fig4, use_container_width=True)

else
    st.info(Upload a CSV file to start analyzing sales data.)