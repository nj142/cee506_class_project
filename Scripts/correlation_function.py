import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import os

def calculate_ao_correlation_per_month(ao_indices, community_raster, years):
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
    for year in years:
        if year not in community_raster:
            continue

        avg_temp = np.mean(community_raster[year])
        for month, ao_value in ao_indices.loc[year].items():
            correlation, p_value = pearsonr([avg_temp], [ao_value]) if not np.isnan(avg_temp) else (np.nan, np.nan)
            results.append({
                "Year": year,
                "Month": month,
                "Correlation": correlation,
                "P-Value": p_value
            })

    return pd.DataFrame(results)


def calculate_enso_correlation_per_month(enso_indices, community_raster, years):
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
    for year in years:
        if year not in community_raster:
            continue

        avg_temp = np.mean(community_raster[year])
        for month, enso_value in enso_indices.loc[year].items():
            correlation, p_value = pearsonr([avg_temp], [enso_value]) if not np.isnan(avg_temp) else (np.nan, np.nan)
            results.append({
                "Year": year,
                "Month": month,
                "Correlation": correlation,
                "P-Value": p_value
            })

    return pd.DataFrame(results)


def plot_heatmap(correlation_raster, community_name, variable, output_dir):
    """
    Plot and save heatmap for spatial correlations.

    Args:
        correlation_raster (2D array): Correlation raster.
        community_name (str): Community name.
        variable (str): AO or ENSO.
        output_dir (str): Directory to save heatmaps.
    """
    os.makedirs(output_dir, exist_ok=True)
    plt.imshow(correlation_raster, cmap="coolwarm", vmin=-1, vmax=1)
    plt.colorbar(label=f"{variable} Correlation")
    plt.title(f"{variable} Correlation Heatmap - {community_name}")
    plt.savefig(os.path.join(output_dir, f"{community_name}_{variable}_heatmap.png"))
    plt.close()


def plot_yearly_correlation(results, community_name, variable, output_dir):
    """
    Plot and save yearly correlation line graphs.

    Args:
        results (DataFrame): DataFrame with columns ['Year', 'Correlation'].
        community_name (str): Community name.
        variable (str): AO or ENSO.
        output_dir (str): Directory to save line graphs.
    """
    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.plot(results["Year"], results["Correlation"], marker="o", label=f"{variable} Correlation")
    plt.title(f"{variable} Yearly Correlation for {community_name}")
    plt.xlabel("Year")
    plt.ylabel("Correlation Coefficient")
    plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)  # Reference line at 0
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, f"{community_name}_{variable}_correlation.png"))
    plt.close()
