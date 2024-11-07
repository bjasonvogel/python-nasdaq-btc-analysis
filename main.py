# -*- coding: utf-8 -*-
import pricechart
import nasdaqextract
import analyzedata
import inputdaterange

# Get date range
start_date, end_date = inputdaterange.GetDates()

# Extract the data
BTC_price_history = nasdaqextract.GetBTCData(start_date, end_date)
        
# Create a time series of prices
pricechart.BuildPriceChart(BTC_price_history, start_date, end_date)

# Do some analytics
analyzedata.Analyze(BTC_price_history)
