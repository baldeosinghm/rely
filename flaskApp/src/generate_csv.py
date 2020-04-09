#!/usr/bin/env python
import csv, json, sys
import requests


def stock_csv(stock):
    try:
        endpoint = requests.get("https://www.quandl.com/api/v3/datasets/WIKI/" + stock + "/data.json?api_key=2KD9BWkNZjPX8SWq7kF7")
        print(endpoint)
        wtd_json = endpoint.json()
        test_file = open("csv/" + stock + ".csv", 'w+')
        test_file.write("Date, Open, High, Low\n")
        for d in wtd_json['dataset_data']['data']:
            test_file.write(f'{d[0]}, {d[1]}, {d[2]}, {d[3]}\n')
        test_file.close()
        return False
    except Exception as e:
        raise
