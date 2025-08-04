# Team Collaboration Practice – Stock Price Prediction

This project demonstrates team collaboration through a practical implementation of **stock price prediction** using Python.

## Project Structure

```plaintext
team-collaboration-practice-main/
├── Stock_Price_Prediction.ipynb # Main Jupyter notebook for modeling and analysis
├── macro_data.py # Script for fetching or processing macroeconomic indicators
└── main_companies_stock.py # Script for handling stock data of major companies
```

## Features

- Time series prediction using historical stock prices
- Integration of in-depth analysis on prediction
- Modular code structure for easy collaboration


## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/team-collaboration-practice.git
   cd team-collaboration-practice
   ```

2. **Run the Notebook:**
Open `Stock_Price_Prediction.ipynb` in Jupyter Lab or Notebook and execute the cells.


## 📊 US Macroeconomic Indicator Viewer

An interactive Streamlit web application for visualizing key **U.S. macroeconomic indicators** using real-time data from [FRED (Federal Reserve Economic Data)](https://fred.stlouisfed.org/). No API key required. Quickly view trends, analyze recent data, and download time series data in CSV format.

---

## 🚀 Features

- ✅ Real-time data pulled from FRED using `pandas_datareader`
- 📅 Custom date range selection
- 📈 Interactive visualizations with Matplotlib
- 🔍 Recent data table preview
- 📥 One-click CSV download

---

## 📦 Included Indicators

| Indicator                | FRED Code  | Description                                                                 |
|--------------------------|------------|-----------------------------------------------------------------------------|
| GDP (US)                 | `GDP`      | Gross Domestic Product (quarterly, in billions of dollars)                 |
| Consumer Price Index     | `CPIAUCNS` | Measures average change in prices paid by consumers (inflation)           |
| Unemployment Rate        | `UNRATE`   | Percentage of the labor force currently unemployed                         |
| Federal Funds Rate       | `FEDFUNDS` | Overnight lending interest rate between depository institutions            |

---

## 🖥️ How It Works

### 1. **User Interface**
- Streamlit page layout with a clean UI and title.
- Dropdown to select an economic indicator.
- Description of the selected indicator is shown alongside.

### 2. **Date Selection**
- Sidebar inputs allow users to select start and end dates.
- Default: January 1, 2010 to today.

### 3. **Data Fetching**
- Data is pulled directly from the FRED API using `pandas_datareader`.
- NaN values are dropped to ensure clean plotting.

### 4. **Visualization**
- Matplotlib is used to plot trends over time.
- Graph includes grid lines, date formatting, and labels.

### 5. **Recent Data Table**
- Shows the latest 10 values in a scrollable table using `st.dataframe()`.

### 6. **Download Option**
- Users can download the dataset as a `.csv` file with one click.

### 7. **Error Handling**
- Errors during data retrieval are gracefully handled and displayed with `st.error()`.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit**
- **pandas**
- **matplotlib**
- **pandas_datareader**



# 📈 Real-Time Stock Price Viewer

A Streamlit web application to view historical stock prices and current market data using **Yahoo Finance** via the `yfinance` Python library. Users can select a company, define a date range, and visualize closing prices over time with built-in Matplotlib plots.

---

## 🚀 Features

- 🔍 Fetch real-time and historical stock data from Yahoo Finance
- 📅 Interactive date selection sidebar
- 📊 Closing price visualization with Matplotlib
- 💹 Displays key stock metrics: Open, High, Low, Close, and Volume
- 📌 Live display of the latest close price

---

## 💼 Available Companies

The app includes popular stocks by default. More can be added easily in the code.

| Company      | Ticker Symbol |
|--------------|----------------|
| Apple        | `AAPL`         |
| Microsoft    | `MSFT`         |
| Tesla        | `TSLA`         |
| Amazon       | `AMZN`         |
| Google       | `GOOGL`        |
| NVIDIA       | `NVDA`         |

---

## 🖥️ How It Works

### 1. **App Layout & Setup**
- Streamlit configures the page title and layout.
- The app displays a title and brief intro.

### 2. **Company Selection**
- A dropdown menu lists supported companies.
- Internally maps the user-friendly name to the actual ticker symbol.

### 3. **Date Range Selection**
- A sidebar widget lets users choose start and end dates.
- Default: from `2023-01-01` to the current date.

### 4. **Data Fetching**
- Uses `yfinance.Ticker().history()` to get historical stock prices for the selected range.

### 5. **Metrics & Table**
- Displays the latest closing price using `st.metric()`.
- Shows a table with daily **Open, High, Low, Close, and Volume** values.

### 6. **Plotting**
- Uses Matplotlib to plot the **closing price trend** over time.
- Interactive and clean chart displayed using `st.pyplot()`.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit**
- **yfinance**
- **pandas**
- **matplotlib**

---



**Data Sources**
- Yahoo Finance via yfinance for stock data
- Manually integrated macroeconomic indicators via macro_data.py

**Contributing**
1. Fork the repository
2. Create your feature branch: git checkout -b feature/my-feature
3. Commit your changes: git commit -am 'Add new feature'
4. Push to the branch: git push origin feature/my-feature
5. Create a new Pull Request

**License**
This project is licensed under the Apache-2.0 License – see the LICENSE file for details.
