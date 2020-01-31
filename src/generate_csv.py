#!/usr/bin/env python
import csv, json, sys
import requests


endpoint = requests.get("https://api.worldtradingdata.com/api/v1/history?symbol=AAPL&sort=newest&api_token=xEA1Hk9dOQ6oesDeipKYWUtefQirEbI1KZnz8RUSNKnXWp5qcF9zqOp7qwvr")
wtd_json = endpoint.json()
test_file = open("../csv/apple.csv", 'w')

for date in wtd_json['history']:
    day = wtd_json['history'][date]
    test_file.write(date + ", " + day['open'] + ", " + day['close'] + ", " + day['high'] + ", " + day['low'] + ", " + day['volume'] + "\n")

test_file.close()
