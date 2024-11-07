# -*- coding: utf-8 -*-
"""
Misc utility functions
"""
from datetime import datetime

#define magic display color text formatting control strings
fmt_green_code = "\033[32m"
fmt_red_code = "\033[31m"
fmt_reset_code = "\033[0m"

"""
Use magic formatting strings to generate red text
"""
def RedText(text_to_format):
    return fmt_red_code + text_to_format + fmt_reset_code

"""
Use magic formatting strings to generate green text
"""
def GreenText(text_to_format):
    return fmt_green_code + text_to_format + fmt_reset_code

"""
Creates a standardized display format to show Percentage Change
"""
def PercentChangeString(pct):
    if pct > 0:
        pct_str = GreenText(f"+{pct:>2.2f}%")
    else:
        pct_str = RedText(f"{pct:>2.2f}%")
    
    return(pct_str)

"""
Extracts key data points from an API result row and
creates a uniform formatted string for display
"""
def DayPriceString(cur_row):
    cur_date = cur_row[0] 
    cur_price = cur_row[1] 
    cur_pct = cur_row[2]
    display = cur_date.strftime("%Y-%m-%d")
    display += "  " + f"${cur_price:>6,.2f}"
    display += " (" + PercentChangeString(cur_pct) + ")"
    return(display)

"""
Creates a uniform formatted string for displaying the selected date range
Option to include or exclude the year
"""
def DateRangeString(sdate, edate, incyear=False):
    if incyear:
        drstr = sdate.strftime("%m/%d/%Y") + " - " + edate.strftime("%m/%d/%Y")
    else:
        drstr = sdate.strftime("%m/%d") + " - " + edate.strftime("%m/%d")   
        
    return drstr

"""
Prompt user for a date
"""
def GetValidDate(inputstr):
    while True:
        user_input = input(inputstr+" (YYYY-MM-DD): ")
        try:
            # Try to parse the input date
            valid_date = datetime.strptime(user_input, "%Y-%m-%d")
            return valid_date.date()
        except ValueError:
            # If parsing fails, prompt the user again
            print(RedText("!!! Invalid date format. Please try again with YYYY-MM-DD."))