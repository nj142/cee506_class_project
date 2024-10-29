import datetime
import pandas as pd

def ReturnAOFetch(years_of_data, ao_data_file_path):
    """
    Function that returns AO indices as a dictionary on a monthly scale 
    from March of start_year-1 to March end_year, reading the file path from input.
    """
    ao_dict = {}

    # Read the text file into pandas DataFrame
    with open(ao_data_file_path, 'r') as f:
        data_lines = f.readlines()

    ao_data = {}
    for line in data_lines[1:]:  # Skipping header
        # yyyy mm1 mm2 mm3 mm4...mm12
        parts = line.strip().split()
        year = int(parts[0])
        ao_values = list(map(float, parts[1:]))

        # Map each month in the current year to the AO value
        for month, ao_value in enumerate(ao_values, start=1):
            date = datetime.datetime(year, month, 1)
            ao_data[date] = ao_value

    for year in years_of_data:
        start_date = datetime.datetime(year - 1, 3, 1)
        end_date = datetime.datetime(year, 3, 1)
        ao_indices = [ao_data[date] for date in ao_data if start_date <= date <= end_date]

        # Store in dictionary
        ao_dict[year] = ao_indices

    return ao_dict