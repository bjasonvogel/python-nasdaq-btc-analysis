# -*- coding: utf-8 -*-
"""
Performs analysis of quantitative data
"""

import functions as fn

volatility_threshold = 4.0

def Analyze(BTC_price_history):
    min_price = min(BTC_price_history, key=lambda row: row[1])
    max_price = max(BTC_price_history, key=lambda row: row[1])
    print("Lowest  Price occured on", fn.DayPriceString(min_price))
    print("Highest Price occured on", fn.DayPriceString(max_price))

    # Identify volitile days
    print("Most volitile days [Defined as change of greater than +/- " + f"{volatility_threshold:>2,.1f}%" + "]")
    volitile_days_index = [index for index, row in enumerate(BTC_price_history) if abs(row[2]) > volatility_threshold]

    for volitile_day in volitile_days_index:
        print(fn.DayPriceString(BTC_price_history[volitile_day]))