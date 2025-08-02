import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stock Price Viewer", layout="centered")

# Title
st.title("📈 Real-Time Stock Price Viewer")
st.write("Get historical and current stock data using Yahoo Finance via Python!")

# Choose a popular company
popular_stocks = {
    "Apple (AAPL)": "AAPL",
    "Microsoft (MSFT)": "MSFT",
    "Tesla (TSLA)": "TSLA",
    "Amazon (AMZN)": "AMZN",
    "Google (GOOGL)": "GOOGL",
    "NVIDIA (NVDA)": "NVDA"
}

company_name = st.selectbox("Select a Company", list(popular_stocks.keys()))
ticker_symbol = popular_stocks[company_name]

# Date selection
st.sidebar.header("📅 Date Range")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# Fetch stock data
st.subheader(f"Stock Data for {company_name}")
ticker_data = yf.Ticker(ticker_symbol)
stock_df = ticker_data.history(start=start_date, end=end_date)

# Show latest stock info
st.metric(label="📌 Latest Close Price", value=f"${stock_df['Close'][-1]:.2f}")

# Display dataframe
st.dataframe(stock_df[['Open', 'High', 'Low', 'Close', 'Volume']])

# Plotting
st.subheader("📊 Closing Price Over Time")
fig, ax = plt.subplots()
ax.plot(stock_df.index, stock_df['Close'], label='Close Price', color='blue')
ax.set_xlabel("Date")
ax.set_ylabel("Price ($)")
ax.set_title(f"{ticker_symbol} Closing Price")
ax.legend()
st.pyplot(fig)
