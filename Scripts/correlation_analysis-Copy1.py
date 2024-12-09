import numpy as np
import pandas as pd
from scipy.stats import pearsonr

def calculate_ao_correlation_per_month(ao_indices, mean_30d_raster_temps, community_names, years):
    """
    Calculate Pearson correlation between AO indices and mean 30-day raster temperatures per month for each community.

    Args:
        ao_indices (DataFrame): AO index values with years as rows and months as columns.
        mean_30d_raster_temps (dict): Dictionary with community names as keys and rasters as values (each raster has yearly mean temperatures).
        community_names (list): List of community names.
        years (list): List of years.

    Returns:
        DataFrame: DataFrame containing community, year, month, correlation coefficient, and p-value.
    """
    results = []

    for community in community_names:
        if community not in mean_30d_raster_temps:
            continue

        # Extract the raster for the current community
        community_raster = mean_30d_raster_temps[community]  
        for year in years:
            if year not in community_raster or year not in ao_indices.index:
                continue

            # mean temperature from the raster for the given year
            avg_temp = np.mean(community_raster[year])

            for month in range(1, 13):  # Iterate over all months
                ao_value = ao_indices.loc[year, month]

                # Calculate correlation
                correlation, p_value = pearsonr([avg_temp], [ao_value]) if not np.isnan(avg_temp) else (np.nan, np.nan)
                results.append({
                    "Community": community,
                    "Year": year,
                    "Month": month,
                    "Correlation": correlation,
                    "P-Value": p_value
                })

    return pd.DataFrame(results)


def calculate_enso_correlation_per_month(enso_indices, mean_30d_raster_temps, community_names, years):
    """
    Calculate Pearson correlation between ENSO indices and mean 30-day raster temperatures per month for each community.

    Args:
        enso_indices (DataFrame): ENSO index values with years as rows and months as columns.
        mean_30d_raster_temps (dict): Dictionary with community names as keys and rasters as values (each raster has yearly mean temperatures).
        community_names (list): List of community names.
        years (list): List of years.

    Returns:
        DataFrame: DataFrame containing community, year, month, correlation coefficient, and p-value.
    """
    results = []

    for community in community_names:
        if community not in mean_30d_raster_temps:
            continue

        # Extract the raster for the current community
        community_raster = mean_30d_raster_temps[community]  # Assume raster is a dict {year: mean_temperature_array}

        for year in years:
            if year not in community_raster or year not in enso_indices.index:
                continue

            # Get the mean temperature from the raster for the given year
            avg_temp = np.mean(community_raster[year])

            for month in range(1, 13):  # Iterate over all months
                enso_value = enso_indices.loc[year, month]

                # Calculate correlation
                correlation, p_value = pearsonr([avg_temp], [enso_value]) if not np.isnan(avg_temp) else (np.nan, np.nan)
                results.append({
                    "Community": community,
                    "Year": year,
                    "Month": month,
                    "Correlation": correlation,
                    "P-Value": p_value
                })

    return pd.DataFrame(results)
