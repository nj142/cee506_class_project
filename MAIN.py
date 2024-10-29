import datetime

import sys
import os
# Add the parent directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cee506_class_project.Scripts.ao_indices import ReturnAOFetch
from cee506_class_project.Scripts.enso_indices import ReturnENSOFetch
from cee506_class_project.Scripts.sea_ice_indices import CalculateIceIndex

# ------------------------------------------------ #
#                  MAIN CODE                       # 
# ------------------------------------------------ #

# Parameters (This will make a list of 2000-2022, as python excludes the 2nd value)
years_of_data = list(range(2000, 2023))

# ------------------------------------------------ #

# Pull in ENSO data as dictionary of Datetime:Values on a MONTHLY scale from all years of data
# Format of this dictionary should go from march of year-1 to march of year (e.g. year 2000 is dictionary M1999-M2000) for each year
#enso_data_filepath = "../Data/ENSO_index.rtf"
#enso_indices = ReturnENSOFetch(years_of_data, enso_data_filepath)

# Pull in AO data as dictionary of Datetime:Values on a MONTHLY scale from all years of data
# Format of this dictionary should go from march of year-1 to march of year (e.g. year 2000 is dictionary M1999-M2000) for each year
ao_data_filepath = "cee506_class_project/Data/monthly.ao.index.txt"
ao_indices = ReturnAOFetch(years_of_data, ao_data_filepath)

# Find ice index, returned as a dictionary of Datetime:Index
ice_data_filepath = "cee506_class_project/Data/ice_data.csv"
ice_indices = CalculateIceIndex(years_of_data, ice_data_filepath)

# Calculate correlations:
    # For each of the ~200 months in the dictionary of our oscillation indices,
        # Calculate the correlation with the ice index for that year
        # Return a structure of all of those indices to be plotted
#ao_correlation_values = CalculateAOCorrelation(ao_indices, ice_indices)
#enso_correlation_values = CalculateENSOCorrelation(enso_indices, ice_indices)

# Chart Values - Each year is a line with Months A-F on X axis, correlation values on Y axis
#ChartENSOValues(enso_correlation_values)
#ChartAOValues(ao_correlation_values)
