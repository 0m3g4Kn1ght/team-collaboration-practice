import streamlit as st
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="📉 Macro Data Viewer", layout="centered")

# Available indicators (Yahoo FRED-style)
indicators = {
    "GDP (US)": "GDP",
    "Consumer Price Index (CPI)": "CPIAUCNS",
    "Unemployment Rate": "UNRATE",
    "Federal Funds Rate": "FEDFUNDS"
}

st.title("📊 Macroeconomic Indicator Viewer (No API Key Needed)")
st.write("Data is pulled using `pandas_datareader` from FRED via Yahoo")

# Indicator picker
indicator = st.selectbox("Choose an Indicator", list(indicators.keys()))
code = indicators[indicator]

# Date range
st.sidebar.header("📅 Date Range")
start = st.sidebar.date_input("Start Date", datetime(2010, 1, 1))
end = st.sidebar.date_input("End Date", datetime.today())

# Fetch data
try:
    data = web.DataReader(code, 'fred', start, end)
    st.subheader(f"{indicator} ({start} to {end})")
    st.line_chart(data)
    st.dataframe(data.tail())
except Exception as e:
    st.error(f"Error fetching data: {e}")
