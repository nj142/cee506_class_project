import os
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

def parse_indices(file_path):
    """
    Parse AO or ENSO index data from a tabular file with fixed columns for months.
    """
    try:
        # Read the file assuming tabular format with space-separated values
        df = pd.read_csv(
            file_path,
            delim_whitespace=True,  # Handle space-separated values
            index_col=0,  # Use the first column (Year) as the index
            header=0  # Assume the header row is present
        )

        # Ensure the columns match the 12 months
        if len(df.columns) != 12:
            raise ValueError(f"Expected 12 columns for months, but got {len(df.columns)}.")

        # Rename columns to represent months
        df.columns = range(1, 13)  # 1 for Jan, 2 for Feb, ..., 12 for Dec
        return df

    except Exception as e:
        print(f"Error parsing file {file_path}: {e}")
        raise


def calculate_lagged_correlations(indices, months_prior_to_july, ice_data, lag=0):
    results = []

    for community in ice_data['Community'].unique():
        community_data = ice_data[ice_data['Community'] == community]

        correlations = []
        for _, row in community_data.iterrows():
            year = row['Year'] - lag
            breakup_doy = row['Breakup_DOY']

            if year in indices.index:
                monthly_values = indices.loc[year, months_prior_to_july]
                avg_monthly_value = monthly_values.mean()

                correlations.append((breakup_doy, avg_monthly_value))

        if len(correlations) > 1:
            breakup_doys, index_values = zip(*correlations)
            correlation, _ = pearsonr(breakup_doys, index_values)
        else:
            correlation = np.nan

        results.append({'Community': community, 'Correlation': correlation})

    return pd.DataFrame(results)

def save_results_to_csv(results, file_path):
    """
    Save the correlation results to a CSV file.
    """
    results.to_csv(file_path, index=False)
    print(f"Results saved to {file_path}")

def plot_results(results, index_name, save_dir):
    """
    Plot correlation results for each Community and save the plots.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    for _, row in results.iterrows():
        plt.figure(figsize=(6, 4))
        plt.bar(row['Community'], row['Correlation'], color='blue')
        plt.title(f"{index_name} Correlation: {row['Community']}")
        plt.xlabel('Community')
        plt.ylabel('Correlation Coefficient')
        plt.ylim(-1, 1)
        plt.xticks(rotation=90)
        save_path = os.path.join(save_dir, f"{index_name}_correlation_{row['Community']}.png")
        plt.savefig(save_path, dpi=300)
        plt.close()
    print(f"Plots saved to {save_dir}")


def calculate_ao_correlation(site_name, ice_data_filepath, ao_data_filepath, project_root, lag=1):
    """
    Calculate AO correlations for a specific site using indices and breakup data.
    """
    ao_indices = parse_indices(ao_data_filepath)  # Load AO indices
    ice_data = pd.read_csv(ice_data_filepath)  # Load breakup data

    # Filter ice data for this site
    site_ice_data = ice_data[ice_data["Community"] == site_name]

    # Calculate correlations
    ao_correlations = calculate_lagged_correlations(
        ao_indices, months_prior_to_july=range(1, 7), ice_data=site_ice_data, lag=lag
    )

    # Save results
    output_csv = os.path.join(project_root, "Results", f"ao_correlations_{site_name}.csv")
    save_results_to_csv(ao_correlations, output_csv)
    print(f"AO correlations saved for {site_name}")

    return ao_correlations

def calculate_enso_correlation(site_name, ice_data_filepath, enso_data_filepath, project_root, lag=1):
    """
    Calculate ENSO correlations for a specific site using indices and breakup data.
    """
    enso_indices = parse_indices(enso_data_filepath)  # Load ENSO indices
    ice_data = pd.read_csv(ice_data_filepath)  # Load breakup data

    # Filter ice data for this site
    site_ice_data = ice_data[ice_data["Community"] == site_name]

    # Calculate correlations
    enso_correlations = calculate_lagged_correlations(
        enso_indices, months_prior_to_july=range(1, 7), ice_data=site_ice_data, lag=lag
    )

    # Save results
    output_csv = os.path.join(project_root, "Results", f"enso_correlations_{site_name}.csv")
    save_results_to_csv(enso_correlations, output_csv)
    print(f"ENSO correlations saved for {site_name}")

    return enso_correlations