import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import os

def calculate_ao_correlation_per_month(ao_indices, mean_30d_raster_temps, years):
    results = []
    total_avg_temp = []
    total_ao_value = []
    for year in years:
        if year not in ao_indices or year not in mean_30d_raster_temps:
            continue
        print('Processing:', year)

        #Mean temperatures for 13 months
        for month_data in mean_30d_raster_temps[year]:
            month_name = month_data['month_name']
            temp_values = month_data['month_value']
            avg_temp = np.ma.mean(temp_values)
            total_avg_temp.append(avg_temp)
            #print(f"Month: {month_name}, Avg temp: {avg_temp}")
            
        if np.isnan(avg_temp):  # Skip if average temperature is NaN
            continue
        #print(total_avg_temp)
        
        
        #AO indices for 13 months
        for month_data in ao_indices[year]:
            month = month_data["month_name"]
            ao_value = month_data["month_value"]
            total_ao_value.append(ao_value)
            #print(f"Month: {month}, AO Value: {ao_value}")
        #print(total_ao_value)
        
        correlation, p_value = pearsonr(total_avg_temp, total_ao_value)
        #print('correltaion:', correlation)
        #print('p_value:', p_value)
        results.append({
            "Year": year,
            "Month": month,
            "Correlation": correlation,
            "P-Value": p_value
        })
    print(results)
    return pd.DataFrame(results)


def calculate_enso_correlation_per_month(enso_indices, mean_30d_raster_temps, years):
    results = []
    total_avg_temp = []
    total_enso_value = []
    for year in years:
        if year not in enso_indices or year not in mean_30d_raster_temps:
            continue
        print('Processing:', year)

        #Mean temperatures for 13 months
        for month_data in mean_30d_raster_temps[year]:
            month_name = month_data['month_name']
            temp_values = month_data['month_value']
            avg_temp = np.ma.mean(temp_values)
            total_avg_temp.append(avg_temp)
            #print(f"Month: {month_name}, Avg temp: {avg_temp}")
            
        if np.isnan(avg_temp):  # Skip if average temperature is NaN
            continue
        
        
        #AO indices for 13 months
        for month_data in enso_indices[year]:
            month = month_data["month_name"]
            enso_value = month_data["month_value"]
            total_enso_value.append(enso_value)
            #print(f"Month: {month}, AO Value: {ao_value}")
        
        correlation, p_value = pearsonr(total_avg_temp, total_enso_value)
        #print('correltaion:', correlation)
        #print('p_value:', p_value)
        results.append({
            "Year": year,
            "Month": month,
            "Correlation": correlation,
            "P-Value": p_value
        })
    #print(results)
    return pd.DataFrame(results)

def plot_heatmap(monthly_temp, ao_indices, enso_indices):
    
    total_avg_temp = []
    for year in range(2001, 2023):
        if year in monthly_temp and monthly_temp[year] is not None:
            for month_data in monthly_temp[year]:
                month = month_data['month_name']
                temp_values = month_data['month_value']
                avg_temp = np.ma.mean(temp_values)
                total_avg_temp.append({
                    "Year": year,
                    "Month": month,
                    "Avg_temp": avg_temp,
                })
        else:
            print(f"Missing or invalid data for year {year}")
            
    data = []
    for year in total_avg_temp:
        for month in total_avg_temp:
            if year['Year'] == month['Year']:
                avg_temp = month['Avg_temp']
                ao_value = next((item['month_value'] for item in ao_indices[year['Year']] if item['month_name'] == month['Month']), None)
                enso_value = next((item['month_value'] for item in enso_indices[year['Year']] if item['month_name'] == month['Month']), None)
                data.append([year['Year'], month['Month'], avg_temp, ao_value, enso_value])
    
    df = pd.DataFrame(data, columns=['Year', 'Month', 'Avg_temp', 'AO', 'ENSO'])
    
    # Calculate the correlation matrix
    corr_matrix = df[['Avg_temp', 'AO', 'ENSO']].corr()
    
    return corr_matrix


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