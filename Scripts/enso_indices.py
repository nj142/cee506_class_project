import pandas as pd
import matplotlib.pyplot as plt
import re
from datetime import datetime
import json

def ReturnENSOFetch(years_of_data):
    rtf_file_path = '/home/jovyan/work/ESDA_project_past/ENSO_index.rtf'

    #Open the file
    with open(rtf_file_path, 'r', encoding='utf-8') as rtf_file:
        rtf_content = rtf_file.read()

    #(\d+): A sequence of digits
    #\s+: One or more white space
    #[-+]?: + or - in the beginning
    #\d*\.\d+: Floating point numbers
    #\d+: Integer numbers
    #data = re.findall(r'(\d+)\s+([-+]?\d*\.\d+|\d+)(?:\s+([-+]?\d*\.\d+|\d+))*', rtf_content)
    data = re.findall(r'(\d+)\s+((?:[-+]?\d*\.\d+|\d+)(?:\s+[-+]?\d*\.\d+|\s+\d+)*)', rtf_content)
    data_processed = [(year, list(map(float, months.split()))) for year, months in data]

    #print(data_processed)

    #Make a dictionary
    #data_dict = {}

    #for year, monthly_data in data_processed:
    #    for month, value in enumerate(monthly_data, start=1):
    #        data_dict[(int(year), month)] = value
    #print(data_dict)

    #print(data_dict[(2000, 2)])

    #Extract data
    ENSO_index = {}

    #def ReturnENSOFetch(years_of_data):
    for year in years_of_data:
        #print(year)
        ENSO_index_year = []
        for y, m in [(year - 1, month) for month in range(3, 13)] + [(year, month) for month in range(1, 4)]:
            value = data_dict.get((y, m))
            if value is not None:
                date_key = datetime(y, 3, 1)
                ENSO_index_year.append(value)
        #print(ENSO_index)
        #ENSO_index.append(ENSO_index_year)
        ENSO_index[date_key] = ENSO_index_year
    return ENSO_index