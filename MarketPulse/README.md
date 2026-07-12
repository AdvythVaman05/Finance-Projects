# 📈 MarketPulse

MarketPulse is a real-time stock market dashboard built with **FastAPI** and **Streamlit**. It enables users to search for stocks, visualize interactive candlestick charts, analyze technical indicators, and monitor live market data through a clean and responsive interface.

The project follows a modular frontend-backend architecture, making it easy to extend with additional analytics, data providers, or trading features.

---

## Features

### Stock Search
- Search from 2,300+ NSE listed companies.
- Ranked search results for better relevance.
- Company information retrieval.

### Interactive Charts
- Candlestick charts using Plotly.
- Trading Volume visualization.
- Live chart refresh.
- Multiple historical timeframes.
- Multiple candle intervals.

### Technical Indicators
- Exponential Moving Average (EMA)
- Relative Strength Index (RSI)
- MACD
- Bollinger Bands

### Company Dashboard
- Company Name
- Exchange
- Sector
- Industry
- Market Capitalization
- Previous Close
- Open Price
- Day High / Day Low
- 52 Week High / Low
- Dividend Yield
- P/E Ratio

### Watchlist
- Add favourite stocks
- Remove stocks
- Persistent watchlist stored locally

### Utilities
- Market Open / Closed indicator
- CSV Export
- Auto Refresh

---

# Project Architecture

```
MarketPulse
│
├── backend
│   ├── routes
│   ├── services
│   ├── scripts
│   ├── data
│   └── app.py
│
├── frontend
│   ├── components
│   ├── services
│   ├── utils
│   ├── data
│   └── app.py
│
├── requirements.txt
└── README.md
```

---

# Tech Stack

### Backend

- FastAPI
- Uvicorn
- yFinance
- Pandas
- NSELib

### Frontend

- Streamlit
- Plotly

### Data Source

- Yahoo Finance
- NSE Symbol Database (generated using NSELib)

---

# Installation

Clone the repository

```bash
git clone https://github.com/<your_username>/MarketPulse.git

cd MarketPulse
```

Create a virtual environment

Windows

```bash
python -m venv .venv
```

Linux / macOS

```bash
python3 -m venv .venv
```

Activate it

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Backend

Navigate to the backend folder

```bash
cd backend
```

Start FastAPI

```bash
uvicorn app:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Running the Frontend

Navigate to the frontend folder

```bash
cd frontend
```

Run Streamlit

```bash
streamlit run app.py
```

---

# API Endpoints

## Search Stocks

```
GET /search
```

Parameters

```
query
```

---

## Historical Stock Data

```
GET /stock
```

Parameters

```
ticker
period
interval
```

---

## Company Information

```
GET /company
```

Parameters

```
ticker
```

---

# Screenshots

## Dashboard

> *(Add screenshot here after deployment)*

---

## Technical Indicators

> *(Add screenshot here)*

---

## Company Information

> *(Add screenshot here)*

---

# Future Improvements

- Global Stock Database
- NASDAQ + NYSE Full Search
- Cryptocurrency Support
- Forex Dashboard
- News Sentiment Analysis
- Portfolio Tracking
- Watchlist Synchronization
- Price Alerts
- TradingView Lightweight Charts
- Docker Deployment

---

# Why this project?

MarketPulse was built as an introductory financial analytics project to explore:

- Financial market data pipelines
- FastAPI backend development
- Streamlit dashboards
- Technical analysis
- Interactive financial visualizations
- Modular software architecture

The project serves as the foundation for more advanced quantitative finance and machine learning applications.

---

# License

This project is licensed under the MIT License.

---

# Author

**Advyth Vaman Akalankam**

GitHub: https://github.com/<your_username>

LinkedIn: https://linkedin.com/in/<your_linkedin>   