import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import os


def calculate_ao_correlation_per_month(ao_indices, mean_30d_raster_temps, years):
    """
    Calculate Pearson correlation between AO indices and mean 30-day raster temperatures per month.

    Args:
        ao_indices (DataFrame): AO index values with years as rows and months as columns.
        mean_30d_raster_temps (dict): Dictionary with years as keys and 30-day mean raster temperatures as values.
        years (list): List of years.

    Returns:
        DataFrame: DataFrame containing year, month, correlation coefficient, and p-value.
    """
    results = []

    for year in years:
        if year not in mean_30d_raster_temps or year not in ao_indices.index:
            continue

        avg_temp = np.mean(mean_30d_raster_temps[year])
        for month, ao_value in ao_indices.loc[year].items():
            correlation, p_value = pearsonr([avg_temp], [ao_value]) if not np.isnan(avg_temp) else (np.nan, np.nan)
            results.append({
                "Year": year,
                "Month": month,
                "Correlation": correlation,
                "P-Value": p_value
            })

    return pd.DataFrame(results)


def calculate_enso_correlation_per_month(enso_indices, mean_30d_raster_temps, years):
    """
    Calculate Pearson correlation between ENSO indices and mean 30-day raster temperatures per month.

    Args:
        enso_indices (DataFrame): ENSO index values with years as rows and months as columns.
        mean_30d_raster_temps (dict): Dictionary with years as keys and 30-day mean raster temperatures as values.
        years (list): List of years.

    Returns:
        DataFrame: DataFrame containing year, month, correlation coefficient, and p-value.
    """
    results = []

    for year in years:
        if year not in mean_30d_raster_temps or year not in enso_indices.index:
            continue

        avg_temp = np.mean(mean_30d_raster_temps[year])
        for month, enso_value in enso_indices.loc[year].items():
            correlation, p_value = pearsonr([avg_temp], [enso_value]) if not np.isnan(avg_temp) else (np.nan, np.nan)
            results.append({
                "Year": year,
                "Month": month,
                "Correlation": correlation,
                "P-Value": p_value
            })

    return pd.DataFrame(results)


def plot_heatmap(correlation_raster, variable, output_dir):
    """
    Plot and save heatmap for spatial correlations.

    Args:
        correlation_raster (2D array): Correlation raster.
        variable (str): AO or ENSO.
        output_dir (str): Directory to save heatmaps.
    """
    os.makedirs(output_dir, exist_ok=True)
    plt.imshow(correlation_raster, cmap="coolwarm", vmin=-1, vmax=1)
    plt.colorbar(label=f"{variable} Correlation")
    plt.title(f"{variable} Correlation Heatmap")
    plt.savefig(os.path.join(output_dir, f"{variable}_heatmap.png"))
    plt.close()


def plot_yearly_correlation(results, variable, output_dir):
    """
    Plot and save yearly correlation line graphs.

    Args:
        results (DataFrame): DataFrame with columns ['Year', 'Correlation'].
        variable (str): AO or ENSO.
        output_dir (str): Directory to save line graphs.
    """
    os.makedirs(output_dir, exist_ok=True)
    plt.figure(figsize=(10, 6))
    plt.plot(results["Year"], results["Correlation"], marker="o", label=f"{variable} Correlation")
    plt.title(f"{variable} Yearly Correlation")
    plt.xlabel("Year")
    plt.ylabel("Correlation Coefficient")
    plt.axhline(0, color="gray", linestyle="--", linewidth=0.8)  # Reference line at 0
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(output_dir, f"{variable}_correlation.png"))
    plt.close()
