"""
Python script to regroup the data from 3 files. 

The rows were had for interval ~5 minutes but it was not precise. 
We decided to regroup these 3 files in one unique file 
with hourly data instead of 5 minutes interval data.
"""

import pandas as pd

# Read csv
am = pd.read_csv("hemp/airsensor_moisture_0.csv")
at = pd.read_csv("hemp/airsensor_temperature_0.csv")
lm = pd.read_csv("hemp/leafsensor_moisture_0.csv")

# specify the date
am.date = pd.to_datetime(am.date)
at.date = pd.to_datetime(at.date)
lm.date = pd.to_datetime(lm.date)

# group by hours
df = am.groupby(pd.Grouper(key="date", freq='H')).mean()
df['airsensor_temperature'] = at.groupby(pd.Grouper(key="date", freq='H')).mean().airsensor_temperature
df['leafsensor_moisture'] = lm.groupby(pd.Grouper(key="date", freq='H')).mean().leafsensor_moisture

# write
df.to_csv('hemp/data.csv')
