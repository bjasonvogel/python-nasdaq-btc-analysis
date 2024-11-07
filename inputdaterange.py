# -*- coding: utf-8 -*-
"""
Handes user input of date range parameters
"""
import datetime
import functions as fn

def GetDates():
    """
    NOTE: The API only accepts dates up through yesterday. 
    Attempting to call it with today or later throws an error
    """
    max_date = datetime.date.today() - datetime.timedelta(days=1)

    print("---------- Define Parameters ----------")
    start_date = fn.GetValidDate("Starting Date Range")
    end_date = fn.GetValidDate("Ending Date Range")

    # Force end date to MAX allowed date in case user inputs too large a date
    if end_date > max_date:
        end_date = max_date
        print("End date greater than API allows. Resetting to " + end_date.strftime("%Y-%m-%d"))
        
    return start_date, end_date