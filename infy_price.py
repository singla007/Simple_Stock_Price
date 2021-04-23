import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock price App
Below is the closing price and volume of Infosys!
""")

symbol = "Infy"

tickerData = yf.Ticker(symbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)