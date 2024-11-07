# -*- coding: utf-8 -*-
"""
Generates a daily price chart based on extracted data
"""
import matplotlib.pyplot as plt
from matplotlib.dates import ConciseDateFormatter
import pandas as pd
import functions as fn

def BuildPriceChart(BTC_price_history, start_date, end_date):
    # Extract dates and prices from the BTC_price_history list
    btc_dates = [entry[0] for entry in BTC_price_history]
    btc_prices = [entry[1] for entry in BTC_price_history]
    #btc_deltas = [entry[2] for entry in BTC_price_history]
    btc_vols = [entry[3] for entry in BTC_price_history]

    # Create the chart
    fig, ax = plt.subplots()

    # Create a line plot of prices
    ax.plot(btc_dates, btc_prices, linewidth=1.0, color="red", marker="D", markersize=4, label="Price", zorder=2)
    ax.set_title("Daily Price of BTC-USD for " + fn.DateRangeString(start_date, end_date))
    ax.set_facecolor('#BABABA')

    ax.set_xlabel("Date")
    ax.xaxis.set_major_formatter(ConciseDateFormatter(ax.xaxis.get_major_locator()))

    # Create the bar chart of volume
    axv = ax.twinx()
    axv.bar(btc_dates, btc_vols, label="Volume", color="#FF9999", zorder=1)

    # Keep the bars low. Force alternate axis to be much larger than the actual max
    axv.set_ylim(0, max(btc_vols) * 5)

    axv.set_ylabel('')            # Remove the y-axis label
    axv.set_yticklabels([])       # Remove the tick labels
    axv.tick_params(right=False)  # Hide tick marks

    # Deal with layering of the two axes
    ax.set_zorder(axv.get_zorder()+1)
    ax.patch.set_alpha(0.35)

    # Draw vertical lines at the start of each month
    x_dates = pd.date_range(start=start_date, end=end_date, freq='D')
    start_of_months = pd.date_range(start=x_dates.min().replace(day=1), end=x_dates.max(), freq='MS')
    for start in start_of_months:
        ax.axvline(start, color='gray', linestyle='--', linewidth=0.7)

    # General plot formatting
    ax.set_ylabel("Price")
    ax.yaxis.set_major_formatter('${x:,.0f}')
    plt.grid(axis='y', which='both', linestyle='--', linewidth=0.7)
    plt.show()