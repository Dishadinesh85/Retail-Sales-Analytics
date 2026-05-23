import streamlit as st
import pandas as pd

st.title("Retail Sales Analytics Dashboard")
df = pd.read_csv("data/cleaned_data.csv")

st.subheader("Dataset Preview")
st.write(df.head())

category = st.selectbox(
    "Select Product Category",
    df['Product Category'].unique()
)

filtered = df[
    df['Product Category'] == category
]

st.subheader("Sales by Month")

monthly = filtered.groupby(
    'Month'
)['Total Amount'].sum()

st.line_chart(monthly)
