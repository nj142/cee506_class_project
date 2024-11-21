import pandas as pd
from datetime import datetime

def calculate_ao_temp_correlation_monthly(spring_temp_data, ao_dict, breakup_data):
    """
    Calculate correlation between AO index for the 12 months before March
    (excluding current year's March) and spring air temperature for each community.

    Parameters:
        spring_temp_data (pd.DataFrame): Data with ['Community', 'Year', 'Spring_Avg_Temp_C'].
        ao_dict (dict): AO data from ReturnAOFetch with datetime keys and 13-month AO values.
        breakup_data (pd.DataFrame): Data with ['Community', 'Year', 'Breakup_DOY'].

    Returns:
        pd.DataFrame: Correlation results for each community and each lagged month.
    """
    # Merge spring temperatures with breakup data
    merged_spring_data = spring_temp_data.merge(breakup_data, on=["Community", "Year"])
    correlation_results = []

    for community in merged_spring_data['Community'].unique():
        # Filter data for the community
        community_data = merged_spring_data[merged_spring_data['Community'] == community]
        community_ao_temps = []

        for _, row in community_data.iterrows():
            year = row['Year']
            spring_avg_temp = row['Spring_Avg_Temp_C']
            
            # The March 1st key for the year
            march_key = datetime(year, 3, 1)
            if march_key not in ao_dict:
                print(f"Missing AO data for {community}, {year}")
                continue
            
            # Get AO values for the 12 months before March, excluding current year's March
            ao_values = ao_dict[march_key][:12]  # First 12 months in the AO data (previous March to February)
            months_back = list(range(1, 13))  # 1 to 12 months back
            
            # Combine months_back and AO values
            monthly_ao = [{'Months_Back': months_back[i], 'AO_Value': ao_values[i]} for i in range(12)]
            
            # Append spring temperature and AO data
            community_ao_temps.append({'Year': year, 'Spring_Avg_Temp_C': spring_avg_temp, 'Monthly_AO': monthly_ao})
        
        # Calculate correlations for each lagged month
        monthly_correlations = []
        for months_back in range(1, 13):  # 1 to 12 months before March
            ao_values = []
            spring_temps = []

            # Extract AO and spring temperature values for this lag
            for entry in community_ao_temps:
                spring_temp = entry['Spring_Avg_Temp_C']
                ao_value = next(
                    (ao['AO_Value'] for ao in entry['Monthly_AO'] if ao['Months_Back'] == months_back), None
                )
                if pd.notnull(ao_value) and pd.notnull(spring_temp):
                    ao_values.append(ao_value)
                    spring_temps.append(spring_temp)

            # Calculate correlation for this lag if there is enough data
            if len(ao_values) > 1:
                correlation = pd.Series(ao_values).corr(pd.Series(spring_temps))
            else:
                correlation = None
            
            monthly_correlations.append({'Months_Back': months_back, 'Correlation': correlation})
        
        # Append results for each lag
        for result in monthly_correlations:
            correlation_results.append({
                'Community': community,
                'Months_Back': result['Months_Back'],
                'Correlation': result['Correlation']
            })

    return pd.DataFrame(correlation_results)
