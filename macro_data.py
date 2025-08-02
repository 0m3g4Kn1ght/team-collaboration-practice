import streamlit as st
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Page setup
st.set_page_config(page_title="📉 Macro Dashboard", layout="centered")

# Indicator data & descriptions
indicators = {
    "GDP (US)": {
        "code": "GDP",
        "description": "Gross Domestic Product (quarterly, in billions of dollars)."
    },
    "Consumer Price Index (CPI)": {
        "code": "CPIAUCNS",
        "description": "CPI measures average change over time in prices paid by consumers."
    },
    "Unemployment Rate": {
        "code": "UNRATE",
        "description": "Percentage of the labor force that is unemployed."
    },
    "Federal Funds Rate": {
        "code": "FEDFUNDS",
        "description": "Interest rate at which depository institutions lend reserve balances overnight."
    }
}

# Title
st.markdown("## 📊 US Macroeconomic Indicator Viewer")
st.markdown("Real-time data via **pandas_datareader** from FRED (No API key needed)")
st.markdown("---")

# Indicator selection
col1, col2 = st.columns([2, 3])
with col1:
    selected_name = st.selectbox("Choose an Indicator", list(indicators.keys()))
with col2:
    st.write(f"ℹ️ {indicators[selected_name]['description']}")

indicator_code = indicators[selected_name]["code"]

# Date selection
st.sidebar.header("📅 Select Date Range")
start = st.sidebar.date_input("Start Date", datetime(2010, 1, 1))
end = st.sidebar.date_input("End Date", datetime.today())

# Load data
try:
    data = web.DataReader(indicator_code, "fred", start, end)
    data = data.dropna()

    # Plot with Matplotlib
    st.subheader(f"📈 {selected_name} Trend")
    fig, ax = plt.subplots()
    ax.plot(data.index, data[indicator_code], color="#0A9396", linewidth=2)
    ax.set_title(f"{selected_name} from {start.strftime('%Y-%m-%d')} to {end.strftime('%Y-%m-%d')}")
    ax.set_ylabel("Value")
    ax.grid(True, linestyle="--", alpha=0.5)
    st.pyplot(fig)

    # Latest values
    st.markdown("### 🔍 Latest Values")
    st.dataframe(data.tail(10))

    # Download button
    csv = data.to_csv().encode("utf-8")
    st.download_button(
        label="📥 Download Data as CSV",
        data=csv,
        file_name=f"{indicator_code}_data.csv",
        mime="text/csv",
    )

except Exception as e:
    st.error(f"❌ Could not fetch data: {e}")
