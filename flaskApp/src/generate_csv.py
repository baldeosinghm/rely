#!/usr/bin/env python
import csv, json, sys
import requests


def stock_csv(stock):
    # try and except block used to avoid returning error to UI of flask webpage
    try:
        # Use GET request to hit Quandl's API endpoint
        endpoint = requests.get("https://www.quandl.com/api/v3/datasets/WIKI/" + stock + "/data.json?api_key=2KD9BWkNZjPX8SWq7kF7")
        # Store data in JSON format in var wtd_json
        wtd_json = endpoint.json()
        # Create a csv file for stock in folder csv/
        test_file = open("csv/" + stock + ".csv", 'w+')
        # Add four columns to csv file: Date, Open, High, Low
        test_file.write("Date, Open, High, Low\n")
        # Retrieve every data point from the dict dat which is another dict, dataset_data
        for d in wtd_json['dataset_data']['data']:
            # Write strings to the csv file
            test_file.write(f'{d[0]}, {d[1]}, {d[2]}, {d[3]}\n')
        test_file.close()
        return False
    except Exception as e:
        raise
