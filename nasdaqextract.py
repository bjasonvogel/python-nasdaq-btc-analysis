# -*- coding: utf-8 -*-
"""
Extracts data from the NASDAQ service based on a date range

API Documentation: https://data.nasdaq.com/databases/BCHAIN

Requires a config.json file with API_KEY defined

Metrics Codes 
   MKPRU = Market Price USD.   
   ETRAV = Estimated Transaction Vol
"""
import requests
import datetime
import json
import functions as fn

def GetBTCData(start_date, end_date):
    print("Calling Nasdaq service to extract prices for "+fn.DateRangeString(start_date, end_date, True))

    with open("config.json") as f:
        config = json.load(f)
        nasdaq_webkey = config["API_KEY"]
    
    #print("API key derived from config: " + nasdaq_webkey)    
    
    nasdaq_metrics_code = "MKPRU,ETRAV"
    nasdaq_url = "https://data.nasdaq.com/api/v3/datatables/QDL/BCHAIN"

    # Create an empty list for data points
    BTC_price_history = []

    # Loop through each date between start_date and end_date
    current_date = start_date
    row_count = 0
    yesterdays_price = -1.0

    while current_date <= end_date:  
        # Define the query parameters
        params = {
            "date": current_date.strftime("%Y-%m-%d"),
            "code": nasdaq_metrics_code,
            "api_key": nasdaq_webkey
        }
        
        # Send the GET request
        response = requests.get(nasdaq_url, params=params)
        
        if response.status_code != 200:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            break;

        data = response.json()
        todays_price = data['datatable']['data'][0][2]
        todays_volume = data['datatable']['data'][1][2]
        
        # Compute daily change
        if yesterdays_price == -1:
            percent_change = 0
        else:
            percent_change = ((todays_price - yesterdays_price) / yesterdays_price) * 100
            
        BTC_price_history.append([current_date, todays_price, percent_change, todays_volume])
      
        current_date += datetime.timedelta(days=1)  # Increment the date by one day
        row_count += 1
        yesterdays_price = todays_price
        
        if row_count % 10 == 0:
            print("   Fetched",row_count,"rows so far...")
            
    # Process complete - provide summary
    print("Total rows fetched: ", row_count)
    print("---------- Extract Complete ----------")

    return BTC_price_history