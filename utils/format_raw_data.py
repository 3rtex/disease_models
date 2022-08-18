"""
Python script to regroup the data from the sensor files. 

The rows were had for interval ~5 minutes but it was not precise. 
We decided to regroup per hour.
"""

import pandas as pd
import os

outputs = {}

# Read csv
for path, current_dir, files in os.walk("../cucumber/raw/"):
    for file in files:
        maraicher, device, sensor, _ = file.split("_")
        sensor_name = "{}_{}".format(device, sensor)
        input = pd.read_csv(path + file, names=['date', sensor_name])

        # convert to date
        input.date = pd.to_datetime(input.date)
        
        # replace 2062 date
        corrupted = False
        for i, row in input.iterrows():
            if row.date.year == 2022:
                corrupted = False
                last_date = row.date
                continue
            # if not corrupted:  # yet
            #     corrupted = True
            #     diff = row.date - pd.to_timedelta(5, unit='m') - last_date
            #     print("new cycle at {} instead of {} in file {} (last date = {})".format(
            #         row.date, row.date - diff, file, last_date))
            # input.loc[i, 'date'] = row.date - diff

            # not always correct to assume the diff is the same for the next corrupted lines (repeat itself sometimes)
            last_date = last_date + pd.to_timedelta(5, unit='m')
            input.loc[i, 'date'] = last_date

        # create a output dataframe if not already created
        if maraicher not in outputs:
            outputs[maraicher] = input.groupby(
                pd.Grouper(key="date", freq='H')).mean()

        # add the sensor
        outputs[maraicher][sensor_name] = input.groupby(
            pd.Grouper(key="date", freq='H')).mean()[sensor_name]
        

# save output
for maraicher, df in outputs.items():
    df.to_csv('../cucumber/in/data_{}.csv'.format(maraicher))
