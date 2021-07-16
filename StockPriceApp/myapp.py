import streamlit as st
import yfinance as yf
import pandas as pd

# simple header
st.write("""
# Stock Price App

Shown is closing price and volume of Google

""")

# init var w/ ticker i want to get
tickerSymbol = 'GOOGL'

# get data from ticker w/ yfinance
tickerData = yf.Ticker(tickerSymbol)

# retrieve historical price
# period is how often to retrieve data inbetween start and end date
tickerDf = tickerData.history(period='1d', start='2011-7-15', end='2021-7-15')

# line charts of the dataframe close and volume

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
