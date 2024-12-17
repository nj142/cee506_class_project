#!/usr/bin/env python
# coding: utf-8

# ##### 60 day prior for all three variables
# 
# ##### Adjust vmin and vmax

# In[1]:


#Dataset
import datetime

study_site_names = ["Utqiagvik", "Deering", "Nunam Iqua", "Kwigillingok"]
bounding_box = {'Utqiagvik': {'min_lat': 70.39228882500898, 'max_lat': 72.18891117499102, 'min_lon': -159.58909784464944, 'max_lon': -153.98810215535056}, 
                'Deering': {'min_lat': 65.17688882500897, 'max_lat': 66.97351117499102, 'min_lon': -164.93141369763367, 'max_lon': -160.5011863023663}, 
                'Nunam Iqua': {'min_lat': 61.63529882500898, 'max_lat': 63.43192117499101, 'min_lon': -166.78876011782143, 'max_lon': -162.8934598821786}, 
                'Kwigillingok': {'min_lat': 58.97248882500899, 'max_lat': 60.76911117499102, 'min_lon': -164.95823709415603, 'max_lon': -161.37896290584396}}

breakup_doy = {'Utqiagvik': {2000: {'breakup_date': datetime.datetime(2000, 8, 2, 12, 0), 'anomaly_days': 16.065217391304344, 'uncertainty': 1.0, 'breakup_doy': 215.5}, 
                             2001: {'breakup_date': datetime.datetime(2001, 8, 9, 12, 0), 'anomaly_days': 22.065217391304344, 'uncertainty': 7.0, 'breakup_doy': 221.5}, 
                             2002: {'breakup_date': datetime.datetime(2002, 7, 12, 12, 0), 'anomaly_days': -5.934782608695656, 'uncertainty': 1.0, 'breakup_doy': 193.5}, 
                             2003: {'breakup_date': datetime.datetime(2003, 7, 16, 12, 0), 'anomaly_days': -1.934782608695656, 'uncertainty': 1.0, 'breakup_doy': 197.5}, 
                             2004: {'breakup_date': datetime.datetime(2004, 7, 11, 0, 0), 'anomaly_days': -6.434782608695656, 'uncertainty': 2.0, 'breakup_doy': 193.0}, 
                             2005: {'breakup_date': datetime.datetime(2005, 7, 15, 0, 0), 'anomaly_days': -3.434782608695656, 'uncertainty': 2.0, 'breakup_doy': 196.0}, 
                             2006: {'breakup_date': datetime.datetime(2006, 8, 7, 0, 0), 'anomaly_days': 19.565217391304344, 'uncertainty': 4.0, 'breakup_doy': 219.0}, 
                             2007: {'breakup_date': datetime.datetime(2007, 7, 1, 12, 0), 'anomaly_days': -16.934782608695656, 'uncertainty': 1.0, 'breakup_doy': 182.5}, 
                             2008: {'breakup_date': datetime.datetime(2008, 7, 13, 12, 0), 'anomaly_days': -3.934782608695656, 'uncertainty': 1.0, 'breakup_doy': 195.5}, 
                             2009: {'breakup_date': datetime.datetime(2009, 7, 9, 0, 0), 'anomaly_days': -9.434782608695656, 'uncertainty': 6.0, 'breakup_doy': 190.0}, 
                             2010: {'breakup_date': datetime.datetime(2010, 7, 24, 12, 0), 'anomaly_days': 6.065217391304344, 'uncertainty': 1.0, 'breakup_doy': 205.5}, 
                             2011: {'breakup_date': datetime.datetime(2011, 7, 5, 0, 0), 'anomaly_days': -13.434782608695654, 'uncertainty': 2.0, 'breakup_doy': 186.0}, 
                             2012: {'breakup_date': datetime.datetime(2012, 7, 30, 12, 0), 'anomaly_days': 13.065217391304346, 'uncertainty': 3.0, 'breakup_doy': 212.5}, 
                             2013: {'breakup_date': datetime.datetime(2013, 8, 7, 12, 0), 'anomaly_days': 20.065217391304344, 'uncertainty': 1.0, 'breakup_doy': 219.5}, 
                             2014: {'breakup_date': datetime.datetime(2014, 8, 3, 0, 0), 'anomaly_days': 15.565217391304346, 'uncertainty': 8.0, 'breakup_doy': 215.0}, 
                             2015: {'breakup_date': datetime.datetime(2015, 6, 28, 12, 0), 'anomaly_days': -19.934782608695656, 'uncertainty': 1.0, 'breakup_doy': 179.5}, 
                             2016: {'breakup_date': datetime.datetime(2016, 7, 7, 12, 0), 'anomaly_days': -9.934782608695656, 'uncertainty': 1.0, 'breakup_doy': 189.5}, 
                             2017: {'breakup_date': datetime.datetime(2017, 7, 6, 12, 0), 'anomaly_days': -11.934782608695654, 'uncertainty': 5.0, 'breakup_doy': 187.5}, 
                             2018: {'breakup_date': datetime.datetime(2018, 7, 27, 0, 0), 'anomaly_days': 8.565217391304344, 'uncertainty': 4.0, 'breakup_doy': 208.0}, 
                             2019: {'breakup_date': datetime.datetime(2019, 7, 3, 0, 0), 'anomaly_days': -15.434782608695654, 'uncertainty': 4.0, 'breakup_doy': 184.0}, 
                             2020: {'breakup_date': datetime.datetime(2020, 7, 8, 12, 0), 'anomaly_days': -8.934782608695656, 'uncertainty': 1.0, 'breakup_doy': 190.5}, 
                             2021: {'breakup_date': datetime.datetime(2021, 7, 28, 0, 0), 'anomaly_days': 9.565217391304344, 'uncertainty': 14.0, 'breakup_doy': 209.0}, 
                             2022: {'breakup_date': datetime.datetime(2022, 7, 15, 12, 0), 'anomaly_days': -2.934782608695656, 'uncertainty': 3.0, 'breakup_doy': 196.5}}, 
               'Deering': {2000: {'breakup_date': datetime.datetime(2000, 6, 28, 12, 0), 'anomaly_days': 15.84782608695653, 'uncertainty': 1.0, 'breakup_doy': 180.5}, 
                           2001: {'breakup_date': datetime.datetime(2001, 6, 23, 12, 0), 'anomaly_days': 9.84782608695653, 'uncertainty': 23.0, 'breakup_doy': 174.5}, 
                           2002: {'breakup_date': datetime.datetime(2002, 6, 10, 12, 0), 'anomaly_days': -3.1521739130434696, 'uncertainty': 1.0, 'breakup_doy': 161.5}, 
                           2003: {'breakup_date': datetime.datetime(2003, 6, 10, 12, 0), 'anomaly_days': -3.1521739130434696, 'uncertainty': 3.0, 'breakup_doy': 161.5}, 
                           2004: {'breakup_date': datetime.datetime(2004, 6, 2, 0, 0), 'anomaly_days': -10.65217391304347, 'uncertainty': 2.0, 'breakup_doy': 154.0}, 
                           2005: {'breakup_date': datetime.datetime(2005, 6, 13, 12, 0), 'anomaly_days': -0.1521739130434696, 'uncertainty': 1.0, 'breakup_doy': 164.5}, 
                           2006: {'breakup_date': datetime.datetime(2006, 6, 23, 12, 0), 'anomaly_days': 9.84782608695653, 'uncertainty': 3.0, 'breakup_doy': 174.5}, 
                           2007: {'breakup_date': datetime.datetime(2007, 6, 19, 12, 0), 'anomaly_days': 5.84782608695653, 'uncertainty': 1.0, 'breakup_doy': 170.5}, 
                           2008: {'breakup_date': datetime.datetime(2008, 6, 17, 12, 0), 'anomaly_days': 4.84782608695653, 'uncertainty': 7.0, 'breakup_doy': 169.5}, 
                           2009: {'breakup_date': datetime.datetime(2009, 6, 10, 12, 0), 'anomaly_days': -3.1521739130434696, 'uncertainty': 1.0, 'breakup_doy': 161.5}, 
                           2010: {'breakup_date': datetime.datetime(2010, 6, 21, 12, 0), 'anomaly_days': 7.84782608695653, 'uncertainty': 1.0, 'breakup_doy': 172.5}, 
                           2011: {'breakup_date': datetime.datetime(2011, 6, 8, 12, 0), 'anomaly_days': -5.15217391304347, 'uncertainty': 3.0, 'breakup_doy': 159.5}, 
                           2012: {'breakup_date': datetime.datetime(2012, 6, 24, 0, 0), 'anomaly_days': 11.34782608695653, 'uncertainty': 2.0, 'breakup_doy': 176.0}, 
                           2013: {'breakup_date': datetime.datetime(2013, 6, 18, 12, 0), 'anomaly_days': 4.84782608695653, 'uncertainty': 1.0, 'breakup_doy': 169.5}, 
                           2014: {'breakup_date': datetime.datetime(2014, 6, 11, 12, 0), 'anomaly_days': -2.1521739130434696, 'uncertainty': 1.0, 'breakup_doy': 162.5}, 
                           2015: {'breakup_date': datetime.datetime(2015, 6, 1, 12, 0), 'anomaly_days': -12.15217391304347, 'uncertainty': 1.0, 'breakup_doy': 152.5}, 
                           2016: {'breakup_date': datetime.datetime(2016, 5, 31, 12, 0), 'anomaly_days': -12.15217391304347, 'uncertainty': 1.0, 'breakup_doy': 152.5}, 
                           2017: {'breakup_date': datetime.datetime(2017, 6, 14, 12, 0), 'anomaly_days': 0.8478260869565304, 'uncertainty': 1.0, 'breakup_doy': 165.5}, 
                           2018: {'breakup_date': datetime.datetime(2018, 5, 29, 12, 0), 'anomaly_days': -15.15217391304347, 'uncertainty': 1.0, 'breakup_doy': 149.5}, 
                           2019: {'breakup_date': datetime.datetime(2019, 5, 25, 12, 0), 'anomaly_days': -19.15217391304347, 'uncertainty': 1.0, 'breakup_doy': 145.5}, 
                           2020: {'breakup_date': datetime.datetime(2020, 6, 13, 12, 0), 'anomaly_days': 0.8478260869565304, 'uncertainty': 1.0, 'breakup_doy': 165.5}, 
                           2021: {'breakup_date': datetime.datetime(2021, 6, 18, 0, 0), 'anomaly_days': 4.3478260869565295, 'uncertainty': 2.0, 'breakup_doy': 169.0}, 
                           2022: {'breakup_date': datetime.datetime(2022, 6, 23, 12, 0), 'anomaly_days': 9.84782608695653, 'uncertainty': 7.0, 'breakup_doy': 174.5}}, 
               'Nunam Iqua': {2000: {'breakup_date': datetime.datetime(2000, 5, 28, 0, 0), 'anomaly_days': 6.565217391304344, 'uncertainty': 22.0, 'breakup_doy': 149.0}, 
                              2001: {'breakup_date': datetime.datetime(2001, 5, 29, 0, 0), 'anomaly_days': 6.565217391304344, 'uncertainty': 4.0, 'breakup_doy': 149.0}, 
                              2002: {'breakup_date': datetime.datetime(2002, 5, 23, 12, 0), 'anomaly_days': 1.065217391304344, 'uncertainty': 1.0, 'breakup_doy': 143.5}, 
                              2003: {'breakup_date': datetime.datetime(2003, 5, 23, 12, 0), 'anomaly_days': 1.065217391304344, 'uncertainty': 1.0, 'breakup_doy': 143.5}, 
                              2004: {'breakup_date': datetime.datetime(2004, 5, 11, 12, 0), 'anomaly_days': -9.934782608695656, 'uncertainty': 15.0, 'breakup_doy': 132.5}, 
                              2005: {'breakup_date': datetime.datetime(2005, 5, 25, 0, 0), 'anomaly_days': 2.565217391304344, 'uncertainty': 2.0, 'breakup_doy': 145.0}, 
                              2006: {'breakup_date': datetime.datetime(2006, 5, 30, 12, 0), 'anomaly_days': 8.065217391304344, 'uncertainty': 1.0, 'breakup_doy': 150.5}, 
                              2007: {'breakup_date': datetime.datetime(2007, 5, 24, 0, 0), 'anomaly_days': 1.565217391304344, 'uncertainty': 4.0, 'breakup_doy': 144.0}, 
                              2008: {'breakup_date': datetime.datetime(2008, 5, 26, 12, 0), 'anomaly_days': 5.065217391304344, 'uncertainty': 7.0, 'breakup_doy': 147.5}, 
                              2009: {'breakup_date': datetime.datetime(2009, 6, 4, 0, 0), 'anomaly_days': 12.565217391304346, 'uncertainty': 8.0, 'breakup_doy': 155.0}, 
                              2010: {'breakup_date': datetime.datetime(2010, 5, 30, 12, 0), 'anomaly_days': 8.065217391304344, 'uncertainty': 1.0, 'breakup_doy': 150.5}, 
                              2011: {'breakup_date': datetime.datetime(2011, 5, 25, 12, 0), 'anomaly_days': 3.065217391304344, 'uncertainty': 1.0, 'breakup_doy': 145.5}, 
                              2012: {'breakup_date': datetime.datetime(2012, 6, 4, 12, 0), 'anomaly_days': 14.065217391304346, 'uncertainty': 1.0, 'breakup_doy': 156.5}, 
                              2013: {'breakup_date': datetime.datetime(2013, 6, 8, 12, 0), 'anomaly_days': 17.065217391304344, 'uncertainty': 7.0, 'breakup_doy': 159.5}, 
                              2014: {'breakup_date': datetime.datetime(2014, 5, 3, 0, 0), 'anomaly_days': -19.434782608695656, 'uncertainty': 2.0, 'breakup_doy': 123.0}, 
                              2015: {'breakup_date': datetime.datetime(2015, 5, 25, 12, 0), 'anomaly_days': 3.065217391304344, 'uncertainty': 1.0, 'breakup_doy': 145.5}, 
                              2016: {'breakup_date': datetime.datetime(2016, 5, 4, 12, 0), 'anomaly_days': -16.934782608695656, 'uncertainty': 1.0, 'breakup_doy': 125.5}, 
                              2017: {'breakup_date': datetime.datetime(2017, 5, 10, 12, 0), 'anomaly_days': -11.934782608695654, 'uncertainty': 1.0, 'breakup_doy': 130.5}, 
                              2018: {'breakup_date': datetime.datetime(2018, 5, 10, 12, 0), 'anomaly_days': -11.934782608695654, 'uncertainty': 1.0, 'breakup_doy': 130.5}, 
                              2019: {'breakup_date': datetime.datetime(2019, 5, 13, 0, 0), 'anomaly_days': -9.434782608695656, 'uncertainty': 2.0, 'breakup_doy': 133.0}, 
                              2020: {'breakup_date': datetime.datetime(2020, 5, 18, 12, 0), 'anomaly_days': -2.934782608695656, 'uncertainty': 1.0, 'breakup_doy': 139.5}, 
                              2021: {'breakup_date': datetime.datetime(2021, 5, 23, 12, 0), 'anomaly_days': 1.065217391304344, 'uncertainty': 1.0, 'breakup_doy': 143.5}, 
                              2022: {'breakup_date': datetime.datetime(2022, 5, 13, 12, 0), 'anomaly_days': -8.934782608695656, 'uncertainty': 1.0, 'breakup_doy': 133.5}}, 
               'Kwigillingok': {2000: {'breakup_date': datetime.datetime(2000, 5, 18, 12, 0), 'anomaly_days': 14.043478260869565, 'uncertainty': 1.0, 'breakup_doy': 139.5}, 
                                2001: {'breakup_date': datetime.datetime(2001, 5, 14, 12, 0), 'anomaly_days': 9.043478260869565, 'uncertainty': 1.0, 'breakup_doy': 134.5}, 
                                2002: {'breakup_date': datetime.datetime(2002, 5, 7, 0, 0), 'anomaly_days': 1.5434782608695627, 'uncertainty': 12.0, 'breakup_doy': 127.0}, 
                                2003: {'breakup_date': datetime.datetime(2003, 4, 25, 0, 0), 'anomaly_days': -10.456521739130435, 'uncertainty': 2.0, 'breakup_doy': 115.0}, 
                                2004: {'breakup_date': datetime.datetime(2004, 4, 25, 0, 0), 'anomaly_days': -9.456521739130435, 'uncertainty': 2.0, 'breakup_doy': 116.0}, 
                                2005: {'breakup_date': datetime.datetime(2005, 5, 1, 12, 0), 'anomaly_days': -3.956521739130437, 'uncertainty': 1.0, 'breakup_doy': 121.5}, 
                                2006: {'breakup_date': datetime.datetime(2006, 5, 26, 12, 0), 'anomaly_days': 21.043478260869566, 'uncertainty': 1.0, 'breakup_doy': 146.5}, 
                                2007: {'breakup_date': datetime.datetime(2007, 5, 2, 12, 0), 'anomaly_days': -2.9565217391304373, 'uncertainty': 3.0, 'breakup_doy': 122.5}, 
                                2008: {'breakup_date': datetime.datetime(2008, 5, 20, 12, 0), 'anomaly_days': 16.043478260869566, 'uncertainty': 1.0, 'breakup_doy': 141.5}, 
                                2009: {'breakup_date': datetime.datetime(2009, 5, 12, 12, 0), 'anomaly_days': 7.043478260869563, 'uncertainty': 1.0, 'breakup_doy': 132.5}, 
                                2010: {'breakup_date': datetime.datetime(2010, 5, 13, 0, 0), 'anomaly_days': 7.543478260869563, 'uncertainty': 10.0, 'breakup_doy': 133.0}, 
                                2011: {'breakup_date': datetime.datetime(2011, 5, 13, 12, 0), 'anomaly_days': 8.043478260869563, 'uncertainty': 5.0, 'breakup_doy': 133.5}, 
                                2012: {'breakup_date': datetime.datetime(2012, 5, 21, 12, 0), 'anomaly_days': 17.043478260869566, 'uncertainty': 1.0, 'breakup_doy': 142.5}, 
                                2013: {'breakup_date': datetime.datetime(2013, 5, 27, 12, 0), 'anomaly_days': 22.043478260869566, 'uncertainty': 1.0, 'breakup_doy': 147.5}, 
                                2014: {'breakup_date': datetime.datetime(2014, 4, 19, 12, 0), 'anomaly_days': -15.956521739130435, 'uncertainty': 5.0, 'breakup_doy': 109.5}, 
                                2015: {'breakup_date': datetime.datetime(2015, 4, 25, 12, 0), 'anomaly_days': -9.956521739130435, 'uncertainty': 1.0, 'breakup_doy': 115.5}, 
                                2016: {'breakup_date': datetime.datetime(2016, 4, 11, 12, 0), 'anomaly_days': -22.95652173913044, 'uncertainty': 1.0, 'breakup_doy': 102.5}, 
                                2017: {'breakup_date': datetime.datetime(2017, 4, 30, 0, 0), 'anomaly_days': -5.456521739130436, 'uncertainty': 4.0, 'breakup_doy': 120.0}, 
                                2018: {'breakup_date': datetime.datetime(2018, 4, 27, 12, 0), 'anomaly_days': -7.956521739130437, 'uncertainty': 17.0, 'breakup_doy': 117.5}, 
                                2019: {'breakup_date': datetime.datetime(2019, 4, 9, 0, 0), 'anomaly_days': -26.45652173913044, 'uncertainty': 6.0, 'breakup_doy': 99.0}, 
                                2020: {'breakup_date': datetime.datetime(2020, 5, 1, 0, 0), 'anomaly_days': -3.4565217391304373, 'uncertainty': 2.0, 'breakup_doy': 122.0}, 
                                2021: {'breakup_date': datetime.datetime(2021, 5, 10, 0, 0), 'anomaly_days': 4.543478260869564, 'uncertainty': 6.0, 'breakup_doy': 130.0}, 
                                2022: {'breakup_date': datetime.datetime(2022, 4, 26, 12, 0), 'anomaly_days': -8.956521739130437, 'uncertainty': 1.0, 'breakup_doy': 116.5}}}


# In[94]:


import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

colors = {
    'Utqiagvik': "blue",
    'Deering': "green",
    'Kwigillingok': "orange",
}

#Create a map
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([-180, -130, 50, 75], crs=ccrs.PlateCarree())  # Focus on Alaska region

#Add map features
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.STATES, linestyle='--')

#Plot bounding boxes
for name, box in bounding_box.items():
    rect = plt.Rectangle(
        (box['min_lon'], box['min_lat']),
        box['max_lon'] - box['min_lon'],
        box['max_lat'] - box['min_lat'],
        linewidth=2, edgecolor=colors.get(name, "red"), facecolor='none', label=name
    )
    ax.add_patch(rect)

#Add gridlines with labels
gl = ax.gridlines(draw_labels=True, linestyle='--', linewidth=0.5, color='gray')
gl.xlabels_top = False  # Turn off top labels
gl.ylabels_right = False  # Turn off right labels
gl.xlabel_style = {'size': 10, 'color': 'gray'}
gl.ylabel_style = {'size': 10, 'color': 'gray'}

#Add legend
handles, labels = ax.get_legend_handles_labels()
unique_labels = dict(zip(labels, handles))  # Remove duplicate labels
ax.legend(unique_labels.values(), unique_labels.keys(), loc='upper left', fontsize='small')

#Display map
plt.title("Bounding Boxes on Alaska Map")
plt.savefig('bounding boxes.png')
plt.show()


# In[2]:


#Reshape the data
breakup_date = []

for site, years in breakup_doy.items():
    for year, data in years.items():
        breakup_date.append({'site': site, 'breakup_date': data['breakup_date']})


# In[3]:


#'Utqiagvik'
breakup = []
for year in range(2000, 2023):
    breakup_date = breakup_doy['Utqiagvik'][year]['breakup_date']
    breakup_date = breakup_date.replace(hour=0, minute=0, second=0)
    breakup.append(breakup_date)


# In[4]:


#Anomaly list
breakup_anomaly = []
for year in range(2000, 2023):
    anomaly = breakup_doy['Utqiagvik'][year]['anomaly_days']
    breakup_anomaly.append(anomaly)
print(breakup_anomaly)


# In[51]:


#'Kwigillingok'
breakup = []
for year in range(2000, 2023):
    breakup_date = breakup_doy['Kwigillingok'][year]['breakup_date']
    breakup_date = breakup_date.replace(hour=0, minute=0, second=0)
    breakup.append(breakup_date)

#Anomaly list
breakup_anomaly = []
for year in range(2000, 2023):
    anomaly = breakup_doy['Kwigillingok'][year]['anomaly_days']
    breakup_anomaly.append(anomaly)
print(breakup_anomaly)


# In[108]:


#'Nunam Iqua'
breakup = []
for year in range(2000, 2023):
    breakup_date = breakup_doy['Nunam Iqua'][year]['breakup_date']
    breakup_date = breakup_date.replace(hour=0, minute=0, second=0)
    breakup.append(breakup_date)

#Anomaly list
breakup_anomaly = []
for year in range(2000, 2023):
    anomaly = breakup_doy['Nunam Iqua'][year]['anomaly_days']
    breakup_anomaly.append(anomaly)
print(breakup_anomaly)


# In[153]:


#"Deering"
breakup = []
for year in range(2000, 2023):
    breakup_date = breakup_doy['Deering'][year]['breakup_date']
    breakup_date = breakup_date.replace(hour=0, minute=0, second=0)
    breakup.append(breakup_date)

#Anomaly list
breakup_anomaly = []
for year in range(2000, 2023):
    anomaly = breakup_doy['Deering'][year]['anomaly_days']
    breakup_anomaly.append(anomaly)
print(breakup_anomaly)


# In[9]:


import cdsapi
import xarray as xr
import numpy as np

def mean_30d_raster_temps(bounding_box, estimated_breakup_date):
    year = estimated_breakup_date.year
    start_date = estimated_breakup_date - datetime.timedelta(days=30)
    start_month = start_date.month
    start_day = start_date.day
    end_month = estimated_breakup_date.month
    end_day = estimated_breakup_date.day
    
    dataset = "derived-era5-land-daily-statistics"
    request = {
        "variable": ["2m_temperature"],
        "year": year,
        "month": [f"{start_month:02d}", f"{end_month:02d}"] if start_month != end_month else [f"{end_month:02d}"],
        "day": [f"{d:02d}" for d in range(start_day, 32)] if start_month != end_month else [f"{d:02d}" for d in range(start_day, end_day + 1)],
        "daily_statistic": "daily_mean",
        "time_zone": "utc-09:00",
        "frequency": "1_hourly",
        "area": [bounding_box['max_lat'], bounding_box['min_lon'], bounding_box['min_lat'], bounding_box['max_lon']]
    }

    #client = cdsapi.Client()
    #client.retrieve(dataset, request).download("mean_30d_raster_temps.nc")

    print(request)

    return request
    

for site in study_site_names:
    print(site)
    if site in breakup_doy:
        for year, data in breakup_doy[site].items():
            breakup_date = data['breakup_date']
            bounding_data = bounding_box.get(site)
            if bounding_data is not None:
                result = mean_30d_raster_temps(bounding_data, breakup_date)
                print(result)


# In[4]:


import cdsapi

dataset = "reanalysis-era5-pressure-levels-monthly-means"
request = {
    "product_type": ["monthly_averaged_reanalysis"],
    "variable": [
        "fraction_of_cloud_cover",
        "specific_humidity",
        "temperature"
    ],
    "pressure_level": ["1000"],
    "year": [
        "1940", "1941", "1942",
        "1943", "1944", "1945",
        "1946", "1947", "1948",
        "1949", "1950", "1951",
        "1952", "1953", "1954",
        "1955", "1956", "1957",
        "1958", "1959", "1960",
        "1961", "1962", "1963",
        "1964", "1965", "1966",
        "1967", "1968", "1969",
        "1970", "1971", "1972",
        "1973", "1974", "1975",
        "1976", "1977", "1978",
        "1979", "1980", "1981",
        "1982", "1983", "1984",
        "1985", "1986", "1987",
        "1988", "1989", "1990",
        "1991", "1992", "1993",
        "1994", "1995", "1996",
        "1997", "1998", "1999",
        "2000", "2001", "2002",
        "2003", "2004", "2005",
        "2006", "2007", "2008",
        "2009", "2010", "2011",
        "2012", "2013", "2014",
        "2015", "2016", "2017",
        "2018", "2019", "2020",
        "2021", "2022", "2023",
        "2024"
    ],
    "month": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ],
    "time": ["00:00"],
    "data_format": "netcdf",
    "download_format": "unarchived",
    "area": [60.76911117499102, -164.95823709415603, 58.97248882500899, -161.37896290584396]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download("Kwigillingok_raster_monthly.nc")


# In[5]:


import numpy as np
#Normalized_breakup_doy
#'Utqiagvik'
normalized_breakup_doy = {}
for site, years in breakup_doy.items():
    anomaly_days_site = [data['anomaly_days'] for year, data in years.items()]
    
    mean_anomaly_site = np.mean(anomaly_days_site)
    std_anomaly_site = np.std(anomaly_days_site)
    #print(mean_anomaly_site)
    #print(std_anomaly_site)
    
    normalized_breakup_doy[site] = {}
    for year, data in years.items():
        normalized_anomaly_days = (data['anomaly_days'] - mean_anomaly_site) / std_anomaly_site
        normalized_breakup_doy[site][year] = {
            'normalized_anomaly_days': normalized_anomaly_days#,
            #'uncertainty': data['uncertainty'],
            #'breakup_doy': data['breakup_doy']
        }

#print(normalized_breakup_doy)

normalized_breakup = normalized_breakup_doy['Utqiagvik']
print(normalized_breakup)


# In[52]:


#Normalized_breakup_doy
#'Kwigillingok'
normalized_breakup_doy = {}
for site, years in breakup_doy.items():
    anomaly_days_site = [data['anomaly_days'] for year, data in years.items()]
    
    mean_anomaly_site = np.mean(anomaly_days_site)
    std_anomaly_site = np.std(anomaly_days_site)
    #print(mean_anomaly_site)
    #print(std_anomaly_site)
    
    normalized_breakup_doy[site] = {}
    for year, data in years.items():
        normalized_anomaly_days = (data['anomaly_days'] - mean_anomaly_site) / std_anomaly_site
        normalized_breakup_doy[site][year] = {
            'normalized_anomaly_days': normalized_anomaly_days#,
            #'uncertainty': data['uncertainty'],
            #'breakup_doy': data['breakup_doy']
        }

#print(normalized_breakup_doy)

normalized_breakup = normalized_breakup_doy['Kwigillingok']
print(normalized_breakup)


# In[109]:


import numpy as np
#Nunam Iqua
normalized_breakup_doy = {}
for site, years in breakup_doy.items():
    anomaly_days_site = [data['anomaly_days'] for year, data in years.items()]
    
    mean_anomaly_site = np.mean(anomaly_days_site)
    std_anomaly_site = np.std(anomaly_days_site)
    #print(mean_anomaly_site)
    #print(std_anomaly_site)
    
    normalized_breakup_doy[site] = {}
    for year, data in years.items():
        normalized_anomaly_days = (data['anomaly_days'] - mean_anomaly_site) / std_anomaly_site
        normalized_breakup_doy[site][year] = {
            'normalized_anomaly_days': normalized_anomaly_days#,
            #'uncertainty': data['uncertainty'],
            #'breakup_doy': data['breakup_doy']
        }

#print(normalized_breakup_doy)

normalized_breakup = normalized_breakup_doy['Nunam Iqua']
print(normalized_breakup)


# In[154]:


#Deering
import numpy as np
normalized_breakup_doy = {}
for site, years in breakup_doy.items():
    anomaly_days_site = [data['anomaly_days'] for year, data in years.items()]
    
    mean_anomaly_site = np.mean(anomaly_days_site)
    std_anomaly_site = np.std(anomaly_days_site)
    #print(mean_anomaly_site)
    #print(std_anomaly_site)
    
    normalized_breakup_doy[site] = {}
    for year, data in years.items():
        normalized_anomaly_days = (data['anomaly_days'] - mean_anomaly_site) / std_anomaly_site
        normalized_breakup_doy[site][year] = {
            'normalized_anomaly_days': normalized_anomaly_days#,
            #'uncertainty': data['uncertainty'],
            #'breakup_doy': data['breakup_doy']
        }

#print(normalized_breakup_doy)

normalized_breakup = normalized_breakup_doy['Deering']
print(normalized_breakup)


# In[6]:


#Specific humidity
from netCDF4 import Dataset
import numpy as np

fp = '/hpc/home/hk339/ESDA506/data/Utqiagvik_raster_sh_merge.nc'
data = Dataset(fp,'r')
print(data.variables.keys())

#Read as numpy array
#March-August
time = data.variables['valid_time'][:]
lat = data.variables['latitude'][:]
lon = data.variables['longitude'][:]
humidity = data.variables['q'][:]

#Remove the dimension of pressure_level
humidity = humidity.squeeze(axis=1)

#Convert time into datetime.datetime
import datetime
start_date = datetime.datetime(1999,3,1)
dates = [start_date + datetime.timedelta(days=int(day)) for day in time]

#Calculate anomaly
#March to August
months_range = range(2, 9)

monthly_means = {}
for month in months_range:
    month_indices = [i for i, date in enumerate(dates) if date.month == month]
    if len(month_indices) > 0:
        monthly_means[month] = np.mean(humidity[month_indices, :, :], axis=0)
        
humidity_anomalies = np.zeros_like(humidity)
for i, date in enumerate(dates):
    if date.month in months_range:
        humidity_anomalies[i, :, :] = humidity[i, :, :] - monthly_means[date.month]
#print(anomalies)

#Normalize humidity
humidity_anomaly_mean = np.mean(humidity_anomalies)
humidity_anomaly_std = np.std(humidity_anomalies)

humidity_normalized_anomalies = (humidity_anomalies - humidity_anomaly_mean) / humidity_anomaly_std
#print(normalized_anomalies)

#Make a dictionary file to link humidity and date
sh = {}
for i, date in enumerate(dates):
    sh[date] = {
        "humidity": humidity_normalized_anomalies[i, :, :],
        "latitude": lat,
        "longitude": lon,
    }

#for key in list(sh.keys())[:10]:
    #print(f"Date: {key}, Humidity: {sh[key]}")


# In[7]:


#Extract 30d humidities and take a mean
mean_30d_humidity = {}
for i in range(23):
    year = breakup[i].year
    start_date = breakup[i] - datetime.timedelta(days=30)
    #print(start_date)
    start_month = start_date.month
    start_day = start_date.day
    end_month = breakup[i].month
    end_day = breakup[i].day
    
    date_range = [
    start_date + datetime.timedelta(days=x)
    for x in range((breakup[i] - start_date).days + 1)
    ]
    
    humidity_values = []
    for date in date_range:
        if date in sh:
            humidity = sh[date]['humidity']
            humidity_values.append(humidity)

        humidity_values_array = np.array(humidity_values)
        mean_humidity = np.mean(humidity_values_array, axis=0)
        mean_30d_humidity[start_date] = {
        "humidity": mean_humidity,
        "latitude": lat,
        "longitude": lon,
    }
#print(mean_30d_humidity)

humidity_years = []

for year in mean_30d_humidity:
    humidity_data = mean_30d_humidity[year]['humidity']
    humidity_years.append(humidity_data)

humidity_array = np.array(humidity_years)

print(humidity_array.shape)


# In[320]:


#Specific Humidity
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot

study_site = ["Utqiagvik", "Deering", "Nunam_Iqua", "Kwigillingok"]

plt.figure(figsize=(10, 10))

for j, site in enumerate(study_site):

    fp = f'/hpc/home/hk339/ESDA506/data/{site}_raster_sh_merge.nc'
    data = Dataset(fp,'r')
    #print(data.variables.keys())

    #Read as numpy array
    #March-August
    time = data.variables['valid_time'][:]
    lat = data.variables['latitude'][:]
    lon = data.variables['longitude'][:]
    humidity = data.variables['q'][:]

    #Remove the dimension of pressure_level
    humidity = humidity.squeeze(axis=1)

    #Convert time into datetime.datetime
    import datetime
    start_date = datetime.datetime(1999,3,1)
    dates = [start_date + datetime.timedelta(days=int(day)) for day in time]

    #Calculate anomaly
    #March to August
    months_range = range(2, 9)

    monthly_means = {}
    for month in months_range:
        month_indices = [i for i, date in enumerate(dates) if date.month == month]
        if len(month_indices) > 0:
            monthly_means[month] = np.mean(humidity[month_indices, :, :], axis=0)

    humidity_anomalies = np.zeros_like(humidity)
    for i, date in enumerate(dates):
        if date.month in months_range:
            humidity_anomalies[i, :, :] = humidity[i, :, :] - monthly_means[date.month]
    #print(anomalies)

    #Normalize humidity
    humidity_anomaly_mean = np.mean(humidity_anomalies)
    humidity_anomaly_std = np.std(humidity_anomalies)

    humidity_normalized_anomalies = (humidity_anomalies - humidity_anomaly_mean) / humidity_anomaly_std
    #print(normalized_anomalies)

    #Make a dictionary file to link humidity and date
    sh = {}
    for i, date in enumerate(dates):
        sh[date] = {
            "humidity": humidity_normalized_anomalies[i, :, :],
            "latitude": lat,
            "longitude": lon,
        }
 
    #Extract 30d humidity and take a mean
    mean_30d_humidity = {}
    humidity_30d = {}
    sh_30d = []

    for i in range(23):
        year = breakup[i].year
        start_date = breakup[i] - datetime.timedelta(days=60)
        #print(start_date)
        start_month = start_date.month
        start_day = start_date.day
        end_month = breakup[i].month
        end_day = breakup[i].day

        date_range = [
        start_date + datetime.timedelta(days=x)
        for x in range((breakup[i] - start_date).days + 1)
        ]

        humidity_values = []
        humidity_30d_prior = []
        for date in date_range:
            if date in sh:
                humidity = sh[date]['humidity']
                humidity_values.append(humidity)
                humidity_30d_prior.append(sh[date]['humidity'])

            humidity_values_array = np.array(humidity_values)
            mean_humidity = np.mean(humidity_values_array, axis=0)
            mean_30d_humidity[start_date] = {
            "humidity": mean_humidity,
            "latitude": lat,
            "longitude": lon,
        }
            humidity_30d[start_date] = {"humidity": humidity_30d_prior,
            "latitude": lat,
            "longitude": lon,
        }

    for date in humidity_30d:
        sh_30d.append(humidity_30d[date]['humidity'])
        sh_30d_array = np.array(sh_30d)
    #print(sh_30d_array.shape)
    sh_30d_prior = np.mean(sh_30d_array, axis=0)
    #print(sh_30d_prior.shape)

    #mean_30d_prior_sh = sh_30d_prior.squeeze(axis=1)
    #print(mean_30d_prior_temps.shape)

    humidity_years = []

    for year in mean_30d_humidity:
        humidity_data = mean_30d_humidity[year]['humidity']
        humidity_years.append(humidity_data)

    humidity_array = np.array(humidity_years)

    #print(temperatures_array.shape)

    days_prior = list(range(60, -1, -1))
    plt.subplot(2,2,j+1)
    plt.plot(days_prior, np.mean(sh_30d_prior, axis=(1,2)), marker='o')
    plt.title(f'60-day prior Specific Humidity in {site}')
    plt.xlabel('Days before Sea Ice Breakup')
    plt.ylabel('Specific Humidity (g/kg)')
    plt.gca().invert_xaxis()
plt.savefig('60d_sh.png')
plt.show()


# In[8]:


#Reshape
normalized_anomaly = []
for year in range(2000,2023):
    nb = normalized_breakup[year]['normalized_anomaly_days']
    normalized_anomaly.append(nb)
normalized_anomaly_days = np.array(normalized_anomaly)
print(normalized_anomaly_days)


# In[9]:


#Correlations
from scipy.stats import pearsonr
correlation_map = np.empty((humidity_array.shape[1], humidity_array.shape[2]))

for i in range(humidity_array.shape[1]):
    for j in range(humidity_array.shape[2]):
        #Get the humidity values for the current grid point across all years
        humidity_values = humidity_array[:, i, j]
        
        #Calculate the correlation between normalized_anomaly_days and humidity_values for this grid point
        correlation, _ = pearsonr(normalized_anomaly_days, humidity_values)
        
        correlation_map[i, j] = correlation

#print(correlation_map)


# In[10]:


#'Utqiagvik'
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.8, vmax=0.1)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Specific Humidity')
plt.savefig('Utqiagvik_correlations_sh.png')
plt.show()


# In[57]:


# 'Kwigillingok'
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.8, vmax=0.1)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Specific Humidity in Kwigillingok')
plt.savefig('Kwigillingok_correlation_sh.png')
plt.show()


# In[114]:


#Nunam Iqua
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.8, vmax=0.1)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Specific Humidity in Nunam Iqua')
plt.savefig('Nunam_Iqua_correlation_sh.png')
plt.show()


# In[159]:


#Deering
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.8, vmax=0.1)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Specific Humidity in Deering')
plt.savefig('Deering_correlation_sh.png')
plt.show()


# In[91]:


get_ipython().run_cell_magic('bash', '', '~/my_conda_env/bin/ncdump -h\n')


# In[321]:


#Temperature
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot

study_site = ["Utqiagvik", "Deering", "Nunam_Iqua", "Kwigillingok"]

plt.figure(figsize=(10, 10))

for j, site in enumerate(study_site):
    fp = f'/hpc/home/hk339/ESDA506/data/{site}_raster_temps_merge.nc'
    data = Dataset(fp,'r')
    #print(data.variables.keys())

    #Read as numpy array
    #March-August
    time = data.variables['valid_time'][:]
    lat = data.variables['latitude'][:]
    lon = data.variables['longitude'][:]
    temperatures = data.variables['t'][:]
    temps_celcius = temperatures - 273.15
    #Remove the dimension of pressure_level
    temperatures = temperatures.squeeze(axis=1)

    #Convert time into datetime.datetime
    import datetime
    start_date = datetime.datetime(1999,3,1)
    dates = [start_date + datetime.timedelta(days=int(day)) for day in time]

    #Calculate anomaly
    #March to August
    months_range = range(2, 9)

    monthly_means = {}
    for month in months_range:
        month_indices = [i for i, date in enumerate(dates) if date.month == month]
        if len(month_indices) > 0:
            monthly_means[month] = np.mean(temperatures[month_indices, :, :], axis=0)

    temperatures_anomalies = np.zeros_like(temperatures)
    for i, date in enumerate(dates):
        if date.month in months_range:
            temperatures_anomalies[i, :, :] = temperatures[i, :, :] - monthly_means[date.month]
    #print(anomalies)

    #Normalize humidity
    temperatures_anomaly_mean = np.mean(temperatures_anomalies)
    temperatures_anomaly_std = np.std(temperatures_anomalies)

    temperatures_normalized_anomalies = (temperatures_anomalies - temperatures_anomaly_mean) / temperatures_anomaly_std
    #print(normalized_anomalies)

    #Make a dictionary file to link humidity and date
    temps = {}
    for i, date in enumerate(dates):
        temps[date] = {
            "temperatures": temperatures_normalized_anomalies[i, :, :],
            "latitude": lat,
            "longitude": lon,
        }

    t = {}
    for i, date in enumerate(dates):
        t[date] = {
            "temperatures": temps_celcius[i, :, :],
            "latitude": lat,
            "longitude": lon,
        }
        
    #Extract 30d temperatures and take a mean
    mean_30d_temperatures = {}
    temperatures_30d = {}
    temps_30d = []

    for i in range(23):
        year = breakup[i].year
        start_date = breakup[i] - datetime.timedelta(days=60)
        #print(start_date)
        start_month = start_date.month
        start_day = start_date.day
        end_month = breakup[i].month
        end_day = breakup[i].day

        date_range = [
        start_date + datetime.timedelta(days=x)
        for x in range((breakup[i] - start_date).days + 1)
        ]

        temperatures_values = []
        temperatures_30d_prior = []
        for date in date_range:
            if date in sh:
                temperatures = temps[date]['temperatures']
                temperatures_values.append(temperatures)
                temperatures_30d_prior.append(t[date]['temperatures'])

            temperatures_values_array = np.array(temperatures_values)
            mean_temperatures = np.mean(temperatures_values_array, axis=0)
            mean_30d_temperatures[start_date] = {
            "temperatures": mean_temperatures,
            "latitude": lat,
            "longitude": lon,
        }
            temperatures_30d[start_date] = {"temperatures": temperatures_30d_prior,
            "latitude": lat,
            "longitude": lon,
        }

    for date in temperatures_30d:
        temps_30d.append(temperatures_30d[date]['temperatures'])
        temps_30d_array = np.array(temps_30d)
    #print(temps_30d_array.shape)
    temps_30d_prior = np.mean(temps_30d_array, axis=0)
    #print(temps_30d_prior.shape)

    mean_30d_prior_temps = temps_30d_prior.squeeze(axis=1)
    #print(mean_30d_prior_temps.shape)

    temperatures_years = []

    for year in mean_30d_temperatures:
        temperatures_data = mean_30d_temperatures[year]['temperatures']
        temperatures_years.append(temperatures_data)

    temperatures_array = np.array(temperatures_years)

    #print(temperatures_array.shape)

    days_prior = list(range(60, -1, -1))
    plt.subplot(2,2,j+1)
    plt.plot(days_prior, np.mean(mean_30d_prior_temps, axis=(1,2)), marker='o')
    plt.title(f'60-day prior Temperature in {site}')
    plt.xlabel('Days before Sea Ice Breakup')
    plt.ylabel('Surface Air Temperature(℃)')
    plt.gca().invert_xaxis()
plt.savefig('60d_temp.png')
plt.show()


# In[10]:


from netCDF4 import Dataset
import numpy as np
fp = '/hpc/home/hk339/ESDA506/data/Utqiagvik_raster_temps_merge.nc'
data = Dataset(fp,'r')
#print(data.variables.keys())

#Read as numpy array
#March-August
time = data.variables['valid_time'][:]
lat = data.variables['latitude'][:]
lon = data.variables['longitude'][:]
temperatures = data.variables['t'][:]

#Remove the dimension of pressure_level
temperatures = temperatures.squeeze(axis=1)

#Convert time into datetime.datetime
import datetime
start_date = datetime.datetime(1999,3,1)
dates = [start_date + datetime.timedelta(days=int(day)) for day in time]
#Calculate anomaly
#March to August
months_range = range(2, 9)

monthly_means = {}
for month in months_range:
    month_indices = [i for i, date in enumerate(dates) if date.month == month]
    if len(month_indices) > 0:
        monthly_means[month] = np.mean(temperatures[month_indices, :, :], axis=0)

temperatures_anomalies = np.zeros_like(temperatures)
for i, date in enumerate(dates):
    if date.month in months_range:
        temperatures_anomalies[i, :, :] = temperatures[i, :, :] - monthly_means[date.month]
#print(anomalies)

#Normalize humidity
temperatures_anomaly_mean = np.mean(temperatures_anomalies)
temperatures_anomaly_std = np.std(temperatures_anomalies)

temperatures_normalized_anomalies = (temperatures_anomalies - temperatures_anomaly_mean) / temperatures_anomaly_std
#print(normalized_anomalies)

#Make a dictionary file to link humidity and date
temps = {}
for i, date in enumerate(dates):
    temps[date] = {
        "temperatures": temperatures_normalized_anomalies[i, :, :],
        "latitude": lat,
        "longitude": lon,
    }


# In[11]:


#Extract 30d temperatures and take a mean
mean_30d_temperatures = {}

for i in range(23):
    year = breakup[i].year
    start_date = breakup[i] - datetime.timedelta(days=60)
    #print(start_date)
    start_month = start_date.month
    start_day = start_date.day
    end_month = breakup[i].month
    end_day = breakup[i].day
    
    date_range = [
    start_date + datetime.timedelta(days=x)
    for x in range((breakup[i] - start_date).days + 1)
    ]
    
    temperatures_values = []
    
    for date in date_range:
        if date in sh:
            temperatures = temps[date]['temperatures']
            temperatures_values.append(temperatures)

        temperatures_values_array = np.array(temperatures_values)
        mean_temperatures = np.mean(temperatures_values_array, axis=0)
        mean_30d_temperatures[start_date] = {
        "temperatures": mean_temperatures,
        "latitude": lat,
        "longitude": lon,
    }

temperatures_years = []

for year in mean_30d_temperatures:
    temperatures_data = mean_30d_temperatures[year]['temperatures']
    temperatures_years.append(temperatures_data)

temperatures_array = np.array(temperatures_years)

print(temperatures_array.shape)


# In[305]:


#Deering
import matplotlib.pyplot
days_prior = list(range(60, -1, -1))
plt.plot(days_prior, np.mean(mean_30d_prior_temps, axis=(1,2)), marker='o')
plt.title('60-day prior Temperature in Utqiagvik')
plt.xlabel('Days before Sea Ice Breakup')
plt.ylabel('Surface Air Temperature(℃)')
plt.gca().invert_xaxis()
plt.savefig('Utqiagvik_60d_temp.png')
plt.show()


# In[12]:


#Correlations
from scipy.stats import pearsonr
correlation_map = np.empty((temperatures_array.shape[1], temperatures_array.shape[2]))

for i in range(temperatures_array.shape[1]):
    for j in range(temperatures_array.shape[2]):
        #Get the humidity values for the current grid point across all years
        temperatures_values = temperatures_array[:, i, j]
        
        #Calculate the correlation between normalized_anomaly_days and humidity_values for this grid point
        correlation, _ = pearsonr(normalized_anomaly_days, temperatures_values)
        
        correlation_map[i, j] = correlation

#print(correlation_map)


# In[77]:


#Original
#Utqiagvik
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.75, vmax=0)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Temperatures in Utqiagvik')
plt.savefig('Utqiagvik_correlation_temp.png')
plt.show()


# In[14]:


#Utqiagvik
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.75, vmax=0)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Temperatures in Utqiagvik')
plt.savefig('Utqiagvik_correlation_temp.png')
plt.show()


# In[72]:


#'Kwigillingok'
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.75, vmax=0)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Temperatures in Kwigillingok')
plt.savefig('Kwigillingok_correlation_temp.png')

plt.show()


# In[118]:


#Nunam Iqua
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.75, vmax=0)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Temperatures in Nunam Iqua')
plt.savefig('Nunam_Iqua_correlation_temp.png')

plt.show()


# In[163]:


#Deering
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.75, vmax=0)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Temperatures in Deering')
plt.savefig('Deering_correlation_temp.png')
plt.show()


# In[13]:


#Cloud cover
from netCDF4 import Dataset
import numpy as np

fp = '/hpc/home/hk339/ESDA506/data/Utqiagvik_raster_cloud_cover_merge.nc'
data = Dataset(fp,'r')
print(data.variables.keys())

#Read as numpy array
#March-August
time = data.variables['valid_time'][:]
lat = data.variables['latitude'][:]
lon = data.variables['longitude'][:]
cloud_cover = data.variables['cc'][:]

#Remove the dimension of pressure_level
cloud_cover = cloud_cover.squeeze(axis=1)

#Convert time into datetime.datetime
import datetime
start_date = datetime.datetime(1999,3,1)
dates = [start_date + datetime.timedelta(days=int(day)) for day in time]

#Calculate anomaly
#March to August
months_range = range(2, 9)

monthly_means = {}
for month in months_range:
    month_indices = [i for i, date in enumerate(dates) if date.month == month]
    if len(month_indices) > 0:
        monthly_means[month] = np.mean(cloud_cover[month_indices, :, :], axis=0)
        
cloud_cover_anomalies = np.zeros_like(cloud_cover)
for i, date in enumerate(dates):
    if date.month in months_range:
        cloud_cover_anomalies[i, :, :] = cloud_cover[i, :, :] - monthly_means[date.month]
#print(anomalies)

#Normalize humidity
cloud_cover_anomaly_mean = np.mean(cloud_cover_anomalies)
cloud_cover_anomaly_std = np.std(cloud_cover_anomalies)

cloud_cover_normalized_anomalies = (cloud_cover_anomalies - cloud_cover_anomaly_mean) / cloud_cover_anomaly_std
#print(normalized_anomalies)

#Make a dictionary file to link humidity and date
cc = {}
for i, date in enumerate(dates):
    cc[date] = {
        "cloud_cover": cloud_cover_normalized_anomalies[i, :, :],
        "latitude": lat,
        "longitude": lon,
    }


# In[14]:


#Extract 30d temperatures and take a mean
mean_30d_cloud_cover = {}
for i in range(23):
    year = breakup[i].year
    start_date = breakup[i] - datetime.timedelta(days=30)
    #print(start_date)
    start_month = start_date.month
    start_day = start_date.day
    end_month = breakup[i].month
    end_day = breakup[i].day
    
    date_range = [
    start_date + datetime.timedelta(days=x)
    for x in range((breakup[i] - start_date).days + 1)
    ]
    
    cloud_cover_values = []
    for date in date_range:
        if date in sh:
            cloud_cover = cc[date]['cloud_cover']
            cloud_cover_values.append(cloud_cover)

        cloud_cover_values_array = np.array(cloud_cover_values)
        mean_cloud_cover = np.mean(cloud_cover_values_array, axis=0)
        mean_30d_cloud_cover[start_date] = {
        "cloud_cover": mean_cloud_cover,
        "latitude": lat,
        "longitude": lon,
    }
#print(mean_30d_cloud_cover)

cloud_cover_years = []

for year in mean_30d_cloud_cover:
    cloud_cover_data = mean_30d_cloud_cover[year]['cloud_cover']
    cloud_cover_years.append(cloud_cover_data)

cloud_cover_array = np.array(cloud_cover_years)

print(cloud_cover_array.shape)


# In[328]:


#Cloud cover
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot

study_site = ["Utqiagvik", "Deering", "Nunam_Iqua", "Kwigillingok"]

plt.figure(figsize=(10, 10))

for j, site in enumerate(study_site):
    fp = f'/hpc/home/hk339/ESDA506/data/{site}_raster_cloud_cover_merge.nc'
    data = Dataset(fp,'r')
    print(data.variables.keys())

    #Read as numpy array
    #March-August
    time = data.variables['valid_time'][:]
    lat = data.variables['latitude'][:]
    lon = data.variables['longitude'][:]
    cloud_cover = data.variables['cc'][:]

    #Remove the dimension of pressure_level
    cloud_cover = cloud_cover.squeeze(axis=1)

    #Convert time into datetime.datetime
    import datetime
    start_date = datetime.datetime(1999,3,1)
    dates = [start_date + datetime.timedelta(days=int(day)) for day in time]

    #Calculate anomaly
    #March to August
    months_range = range(2, 9)

    monthly_means = {}
    for month in months_range:
        month_indices = [i for i, date in enumerate(dates) if date.month == month]
        if len(month_indices) > 0:
            monthly_means[month] = np.mean(cloud_cover[month_indices, :, :], axis=0)

    cloud_cover_anomalies = np.zeros_like(cloud_cover)
    for i, date in enumerate(dates):
        if date.month in months_range:
            cloud_cover_anomalies[i, :, :] = cloud_cover[i, :, :] - monthly_means[date.month]
    #print(anomalies)

    #Normalize humidity
    cloud_cover_anomaly_mean = np.mean(cloud_cover_anomalies)
    cloud_cover_anomaly_std = np.std(cloud_cover_anomalies)

    cloud_cover_normalized_anomalies = (cloud_cover_anomalies - cloud_cover_anomaly_mean) / cloud_cover_anomaly_std
    #print(normalized_anomalies)

    #Make a dictionary file to link humidity and date
    cc = {}
    for i, date in enumerate(dates):
        cc[date] = {
            "cloud_cover": cloud_cover_normalized_anomalies[i, :, :],
            "latitude": lat,
            "longitude": lon,
        }


        #Extract 30d cloud_cover and take a mean
        mean_30d_cloud_cover = {}
        cloud_cover_30d = {}
        cc_30d = []

    for i in range(23):
        year = breakup[i].year
        start_date = breakup[i] - datetime.timedelta(days=60)
        #print(start_date)
        start_month = start_date.month
        start_day = start_date.day
        end_month = breakup[i].month
        end_day = breakup[i].day

        date_range = [
        start_date + datetime.timedelta(days=x)
        for x in range((breakup[i] - start_date).days + 1)
        ]

        cloud_cover_values = []
        cloud_cover_30d_prior = []
        for date in date_range:
            if date in sh:
                cloud_cover = cc[date]['cloud_cover']
                cloud_cover_values.append(cloud_cover)
                cloud_cover_30d_prior.append(cc[date]['cloud_cover'])

            cloud_cover_values_array = np.array(cloud_cover_values)
            mean_cloud_cover = np.mean(cloud_cover_values_array, axis=0)
            mean_30d_cloud_cover[start_date] = {
            "cloud_cover": mean_cloud_cover,
            "latitude": lat,
            "longitude": lon,
        }
            cloud_cover_30d[start_date] = {"cloud_cover": cloud_cover_30d_prior,
            "latitude": lat,
            "longitude": lon,
        }
            
    for date in cloud_cover_30d:
        cc_30d.append(cloud_cover_30d[date]['cloud_cover'])
        cc_30d_array = np.array(cc_30d)
    #print(temps_30d_array.shape)
    cc_30d_prior = np.mean(cc_30d_array, axis=0)
    print(cc_30d_prior.shape)

    #mean_30d_prior_cc = cc_30d_prior.squeeze(axis=1)
    #print(mean_30d_prior_temps.shape)

    cloud_cover_years = []
    for year in mean_30d_cloud_cover:
        cloud_cover_data = mean_30d_cloud_cover[year]['cloud_cover']
        cloud_cover_years.append(cloud_cover_data)

    cloud_cover_array = np.array(cloud_cover_years)

    #print(temperatures_array.shape)

    days_prior = list(range(60, -1, -1))
    plt.subplot(2,2,j+1)
    plt.plot(days_prior, np.mean(cc_30d_prior, axis=(1,2)), marker='o')
    plt.title(f'60-day prior cloud cover in {site}')
    plt.xlabel('Days before Sea Ice Breakup')
    plt.ylabel('Cloud cover')
    plt.gca().invert_xaxis()
plt.savefig('60d_cc.png')
plt.show()


# In[15]:


#Correlations
from scipy.stats import pearsonr
correlation_map = np.empty((cloud_cover_array.shape[1], cloud_cover_array.shape[2]))

for i in range(cloud_cover_array.shape[1]):
    for j in range(cloud_cover_array.shape[2]):
        #Get the cloud_cover values for the current grid point across all years
        cloud_cover_values = cloud_cover_array[:, i, j]
        
        #Calculate the correlation between normalized_anomaly_days and cloud_cover_values for this grid point
        correlation, _ = pearsonr(normalized_anomaly_days, cloud_cover_values)
        
        correlation_map[i, j] = correlation

#print(correlation_map)


# In[18]:


#Utqiagvik
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.6, vmax=0.5)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Could Cover')
plt.savefig('Utqiagvik_correlation_cloud_cover.png')
plt.show()


# In[76]:


#'Kwigillingok'
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.6, vmax=0.5)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Could Cover in Kwigillingok')
plt.savefig('Kwigillingok_correlation_cloud_cover.png')

plt.show()


# In[122]:


#Nunam Iqua
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.6, vmax=0.5)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Could Cover in Nunam Iqua')
plt.savefig('Nunam_Iqua_correlation_cloud_cover.png')

plt.show()


# In[167]:


#Deering
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

#lon_grid, lat_grid = np.meshgrid(lon, lat)

#contour = plt.contourf(lon_grid, lat_grid, correlation_map, cmap='coolwarm', levels=20)
plt.imshow(correlation_map, cmap='coolwarm', aspect='auto', extent=[lon.min(), lon.max(), lat.min(), lat.max()], vmin=-0.6, vmax=0.5)

#plt.colorbar(contour)
plt.colorbar()

plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.title('Correlation Map Could Cover in Deering')
plt.savefig('Deering_correlation_cloud_cover.png')
plt.show()


# In[168]:


lon_rounded = np.round(lon, 1)


# In[16]:


import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

rows, cols = cloud_cover_array.shape[1:]
slopes = np.zeros((rows, cols))
r_squared = np.zeros((rows, cols))

for i in range(rows):
    for j in range(cols):
        X = cloud_cover_array[:, i, j]
        X = sm.add_constant(X)
        Y = normalized_anomaly_days
        
        model = sm.OLS(Y, X)
        results = model.fit()
        
        slopes[i, j] = results.params[1]
        r_squared[i, j] = results.rsquared


# In[17]:


cloud_cover_coeffs = np.zeros((rows, cols))
temperature_coeffs = np.zeros((rows, cols))
humidity_coeffs = np.zeros((rows, cols))

for i in range(rows):
    for j in range(cols):
        X = np.column_stack([cloud_cover_array[:, i, j], temperatures_array[:, i, j], humidity_array[:, i, j]])
        X = sm.add_constant(X)
        Y = normalized_anomaly_days
        
        model = sm.OLS(Y, X)
        results = model.fit()
        
        r_squared[i, j] = results.rsquared
        cloud_cover_coeffs[i, j] = results.params[1]
        temperature_coeffs[i, j] = results.params[2]
        humidity_coeffs[i, j] = results.params[3] 
        
        #print(f"Grid ({i}, {j}): Params={results.params}, R-squared={results.rsquared}")
#print(cloud_cover_coeffs)
#print(temperature_coeffs)
#print(humidity_coeffs)


# In[22]:


#Utqiagvik
plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(slopes), cmap='coolwarm', origin='upper')
#plt.imshow(np.flipud(cloud_cover_coeffs), cmap='coolwarm', origin='upper')
plt.colorbar(label='Regression Slope')
plt.title('Regression Slope of Cloud Cover vs Breakup Date')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Utqiagvik_slope_cloud_cover.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(r_squared), cmap='viridis', origin='upper', vmin=0.2, vmax=0.7)
plt.colorbar(label='R-squared')
plt.title('R-squared of Cloud Cover vs Breakup Date')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Utqiagvik_r2_cloud_cover.png')
plt.show()


# In[80]:


#'Kwigillingok'
plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(slopes), cmap='coolwarm', origin='upper')
#plt.imshow(np.flipud(cloud_cover_coeffs), cmap='coolwarm', origin='upper')
plt.colorbar(label='Regression Slope')
plt.title('Regression Slope of Cloud Cover vs Breakup Date in Kwigillingok')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Kwigillingok_slope_cloud_cover.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(r_squared), cmap='viridis', origin='upper', vmin=0.2, vmax=0.7)
plt.colorbar(label='R-squared')
plt.title('R-squared of Cloud Cover vs Breakup Date in Kwigillingok')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Kwigillingok_r2_cloud_cover.png')
plt.show()


# In[126]:


#Nunam Iqua
plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(slopes), cmap='coolwarm', origin='upper')
#plt.imshow(np.flipud(cloud_cover_coeffs), cmap='coolwarm', origin='upper')
plt.colorbar(label='Regression Slope')
plt.title('Regression Slope of Cloud Cover vs Breakup Date in Nunam Iqua')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Nunam_Iqua_slope_cloud_cover.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(r_squared), cmap='viridis', origin='upper', vmin=0.2, vmax=0.7)
plt.colorbar(label='R-squared')
plt.title('R-squared of Cloud Cover vs Breakup Date in Nunam Iqua')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Nunam_Iqua_r2_cloud_cover.png')
plt.show()


# In[171]:


#Deering
plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(slopes), cmap='coolwarm', origin='upper')
#plt.imshow(np.flipud(cloud_cover_coeffs), cmap='coolwarm', origin='upper')
plt.colorbar(label='Regression Slope')
plt.title('Regression Slope of Cloud Cover vs Breakup Date in Deering')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Deering_slope_cloud_covr.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(r_squared), cmap='viridis', origin='upper', vmin=0.2, vmax=0.7)
plt.colorbar(label='R-squared')
plt.title('R-squared of Cloud Cover vs Breakup Date in Deering')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Deering_r2_cloud_cover.png')
plt.show()


# In[18]:


import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

rows, cols = temperatures_array.shape[1:]
slopes = np.zeros((rows, cols))
r_squared = np.zeros((rows, cols))

for i in range(rows):
    for j in range(cols):
        X = temperatures_array[:, i, j]
        X = sm.add_constant(X)
        Y = normalized_anomaly_days
        
        model = sm.OLS(Y, X)
        results = model.fit()
        
        slopes[i, j] = results.params[1]
        r_squared[i, j] = results.rsquared


# In[24]:


#Utqiagvik
plt.figure(figsize=(10, 6))
#plt.imshow(np.flipud(slopes), cmap='coolwarm', origin='upper')
plt.imshow(np.flipud(temperature_coeffs), cmap='coolwarm', origin='upper')
plt.colorbar(label='Regression Slope')
plt.title('Regression Slope of Air Temperature vs Breakup Date')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Utqiagvik_slope_temp.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(r_squared), cmap='viridis', origin='upper', vmin=0.05, vmax=0.65)
plt.colorbar(label='R-squared')
plt.title('R-squared of Air Temperature vs Breakup Date')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Utqiagvik_r2_temp.png')
plt.show()


# In[83]:


#'Kwigillingok'
plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(slopes), cmap='coolwarm', origin='upper')
#plt.imshow(np.flipud(temperature_coeffs), cmap='coolwarm', origin='upper')
plt.colorbar(label='Regression Slope')
plt.title('Regression Slope of Air Temperature vs Breakup Date in Kwigillingok')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Kwigillingok_slope_temp.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(r_squared), cmap='viridis', origin='upper', vmin=0.05, vmax=0.65)
plt.colorbar(label='R-squared')
plt.title('R-squared of Air Temperature vs Breakup Date in Kwigillingok')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Kwigillingok_r2_temp.png')
plt.show()


# In[128]:


#Nunam Iqua
plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(slopes), cmap='coolwarm', origin='upper')
#plt.imshow(np.flipud(temperature_coeffs), cmap='coolwarm', origin='upper')
plt.colorbar(label='Regression Slope')
plt.title('Regression Slope of Air Temperature vs Breakup Date in Nunam Iqua')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Nunam_Iqua_slope_temp.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(r_squared), cmap='viridis', origin='upper', vmin=0.05, vmax=0.65)
plt.colorbar(label='R-squared')
plt.title('R-squared of Air Temperature vs Breakup Date in Nunam Iqua')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Nunam_Iqua_r2_temp.png')
plt.show()


# In[173]:


#Deering
plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(slopes), cmap='coolwarm', origin='upper')
#plt.imshow(np.flipud(temperature_coeffs), cmap='coolwarm', origin='upper')
plt.colorbar(label='Regression Slope')
plt.title('Regression Slope of Air Temperature vs Breakup Date in Deering')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Deering_slope_temp.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(r_squared), cmap='viridis', origin='upper', vmin=0.05, vmax=0.65)
plt.colorbar(label='R-squared')
plt.title('R-squared of Air Temperature vs Breakup Date in Deering')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Deering_r2_temp.png')
plt.show()


# In[19]:


import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

rows, cols = humidity_array.shape[1:]
slopes = np.zeros((rows, cols))
r_squared = np.zeros((rows, cols))

for i in range(rows):
    for j in range(cols):
        X = humidity_array[:, i, j]
        X = sm.add_constant(X)
        Y = normalized_anomaly_days
        
        model = sm.OLS(Y, X)
        results = model.fit()
        
        slopes[i, j] = results.params[1]
        r_squared[i, j] = results.rsquared


# In[27]:


#Utqiagvik
plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(slopes), cmap='coolwarm', origin='upper')
#plt.imshow(np.flipud(humidity_coeffs), cmap='coolwarm', origin='upper')
plt.colorbar(label='Regression Slope')
plt.title('Regression Slope of Humidity vs Breakup Date')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Utqiagvik_slope_humidity.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(r_squared), cmap='viridis', origin='upper', vmin=0.01, vmax=0.65)
plt.colorbar(label='R-squared')
plt.title('R-squared of Humidity vs Breakup Date')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Utqiagvik_r2_humidity.png')
plt.show()


# In[85]:


#'Kwigillingok'
plt.figure(figsize=(10, 6))
#plt.imshow(np.flipud(slopes), cmap='coolwarm', origin='upper')
plt.imshow(np.flipud(humidity_coeffs), cmap='coolwarm', origin='upper')
plt.colorbar(label='Regression Slope')
plt.title('Regression Slope of Humidity vs Breakup Date in Kwigillingok')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Kwigillingok_slope_sh.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(r_squared), cmap='viridis', origin='upper', vmin=0.01, vmax=0.65)
plt.colorbar(label='R-squared')
plt.title('R-squared of Humidity vs Breakup Date in Kwigillingok')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Kwigillingok_r2_sh.png')
plt.show()


# In[130]:


#Nunam Iqua
plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(slopes), cmap='coolwarm', origin='upper')
#plt.imshow(np.flipud(humidity_coeffs), cmap='coolwarm', origin='upper')
plt.colorbar(label='Regression Slope')
plt.title('Regression Slope of Humidity vs Breakup Date in Nunam Iqua')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Nunam_Iqua_slope_sh.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(r_squared), cmap='viridis', origin='upper', vmin=0.01, vmax=0.65)
plt.colorbar(label='R-squared')
plt.title('R-squared of Humidity vs Breakup Date in Nunam Iqua')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Nunam_Iqua_r2_sh.png')
plt.show()


# In[175]:


#Deering
plt.figure(figsize=(10, 6))
#plt.imshow(np.flipud(slopes), cmap='coolwarm', origin='upper')
plt.imshow(np.flipud(humidity_coeffs), cmap='coolwarm', origin='upper')
plt.colorbar(label='Regression Slope')
plt.title('Regression Slope of Humidity vs Breakup Date in Deering')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Deering_slope_sh.png')
plt.show()

plt.figure(figsize=(10, 6))
plt.imshow(np.flipud(r_squared), cmap='viridis', origin='upper', vmin=0.01, vmax=0.65)
plt.colorbar(label='R-squared')
plt.title('R-squared of Humidity vs Breakup Date in Deering')
plt.xticks(ticks=range(len(lon)), labels=[f'{l:.1f}' for l in lon_rounded], rotation=45)
plt.yticks(ticks=range(len(lat)), labels=lat) 
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('Deering_r2_sh.png')
plt.show()


# In[20]:


from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression

cloud_cover_flat = cloud_cover_array.reshape(23, -1)
temperatures_flat = temperatures_array.reshape(23, -1)
humidity_flat = humidity_array.reshape(23, -1)

pca_cloud_cover = PCA(n_components=5)
pca_temperatures = PCA(n_components=5)
pca_humidity = PCA(n_components=5)

cloud_cover_pca = pca_cloud_cover.fit_transform(cloud_cover_flat)
temperatures_pca = pca_temperatures.fit_transform(temperatures_flat)
humidity_pca = pca_humidity.fit_transform(humidity_flat)

reg = LinearRegression()
#X = np.hstack([cloud_cover_pca])
#X = np.hstack([temperatures_pca])
#X = np.hstack([humidity_pca])
#X = np.hstack([cloud_cover_pca, temperatures_pca])
#X = np.hstack([cloud_cover_pca, humidity_pca])
#X = np.hstack([temperatures_pca, humidity_pca])
X = np.hstack([cloud_cover_pca, temperatures_pca, humidity_pca])
y = normalized_anomaly_days

reg.fit(X, y)


# In[21]:


explained_variance_cloud = np.cumsum(pca_cloud_cover.explained_variance_ratio_)
explained_variance_temp = np.cumsum(pca_temperatures.explained_variance_ratio_)
explained_variance_humidity = np.cumsum(pca_humidity.explained_variance_ratio_)

print("Cloud Cover cumulative explained variance (PC1 to PC5):", explained_variance_cloud[-1])
print("Temperatures cumulative explained variance (PC1 to PC5):", explained_variance_temp[-1])
print("Humidity cumulative explained variance (PC1 to PC5):", explained_variance_humidity[-1])


# In[24]:


#Utqiagvik
print("Regression coefficience:", reg.coef_)

y_pred = reg.predict(X)

import matplotlib.pyplot as plt
plt.plot(y, label='Observed breakup date')
plt.plot(y_pred, label='Expected breakup date')
plt.title('Prediction of breakup anomaly in Utqiagvik')
plt.xlabel('Year')
plt.ylabel('Standardized breakup date anomaly')
plt.legend(loc='upper right')
plt.savefig('Utqiagvik_prediction.png')
plt.show()


# In[106]:


#'Kwigillingok'
print("Regression coefficience:", reg.coef_)

y_pred = reg.predict(X)

import matplotlib.pyplot as plt
plt.plot(y, label='Observed breakup date')
plt.plot(y_pred, label='Expected breakup date')
plt.title('Prediction of breakup anomaly in Kwigillingok')
plt.xlabel('Year')
plt.ylabel('Standardized breakup date anomaly')
plt.legend(loc='upper right')
#plt.savefig('Kwigillingok_prediction.png')
plt.show()


# In[151]:


#Nunam Iqua
print("Regression coefficience:", reg.coef_)

y_pred = reg.predict(X)

import matplotlib.pyplot as plt
plt.plot(y, label='Observed breakup date')
plt.plot(y_pred, label='Expected breakup date')
plt.title('Prediction of breakup anomaly in Nunam Iqua')
plt.xlabel('Year')
plt.ylabel('Standardized breakup date anomaly')
plt.legend(loc='upper right')
#plt.savefig('Nunam_Iqua_prediction.png')
plt.show()


# In[187]:


#Deering
print("Regression coefficience:", reg.coef_)

y_pred = reg.predict(X)

import matplotlib.pyplot as plt
plt.plot(y, label='Observed breakup date')
plt.plot(y_pred, label='Expected breakup date')
plt.title('Prediction of breakup anomaly in Deering')
plt.xlabel('Year')
plt.ylabel('Standardized breakup date anomaly')
plt.legend(loc='upper right')
#plt.savefig('Deering_prediction.png')
plt.show()


# In[50]:


#Utqiagvik
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error
import numpy as np


mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)
mape = mean_absolute_percentage_error(y, y_pred)

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"R²: {r2}")
print(f"MAPE: {mape}")
#Temp(0.6598333321940675) -> cloud cover(0.31995133293988953) -> speficit humidity(0.5417169241936942)
#temp&cc(0.8687007876764287) temps&sh(0.8003527650290814) cc&sh(0.6880416915625507)
#0.9115626574060025
#0.939028489362477


# In[107]:


#'Kwigillingok'
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error
import numpy as np


mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)
mape = mean_absolute_percentage_error(y, y_pred)

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"R²: {r2}")
print(f"MAPE: {mape}")
#Temp(0.5298552799474958) -> cloud cover(0.4486138529991113) -> speficit humidity(0.47637877429893516)
#temp&cc(0.7202808747580447) temps&sh(0.7082069460033946) cc&sh(0.8951241912462479)
#0.9282942004108222
#0.9391048266282341


# In[152]:


#Nunam Iqua
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error
import numpy as np


mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)
mape = mean_absolute_percentage_error(y, y_pred)

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"R²: {r2}")
print(f"MAPE: {mape}")

#Temp(0.5095730329152277) -> cloud cover(0.117584030130646) -> speficit humidity(0.27702524679609686)
#temp&cc(0.5852777735146458) temps&sh(0.5414101768585691) cc&sh(0.5424978556401784)
#0.7978891741238775
#0.6660169619113563


# In[188]:


#Deering
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, mean_absolute_percentage_error
import numpy as np


mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)
mape = mean_absolute_percentage_error(y, y_pred)

print(f"MAE: {mae}")
print(f"MSE: {mse}")
print(f"RMSE: {rmse}")
print(f"R²: {r2}")
print(f"MAPE: {mape}")

#Temp(0.7343718911398787) -> cloud cover(0.4405015181092351) -> speficit humidity(0.7635983404028337)
#temp&cc(0.8276838273763957) temps&sh(0.8983421547113096) cc&sh(0.8088241580965565)
#0.9091200941515332


# In[182]:


import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
for i in range(5):
    plt.subplot(2,3,i+1)
    plt.plot(humidity_pca[:, i], label=f"PC{i+1} (Humidity)")
    plt.xlabel("Time (index)")
    plt.ylabel("Principal Component Value")
    plt.legend()
plt.title("Time Series of PCA Components for Humidity")
plt.tight_layout()
plt.show()


# In[186]:


fig, ax = plt.subplots(3, 2, figsize=(12, 18))

for i in range(5):
    eof = pca_cloud_cover.components_[i].reshape(n_lat, n_lon)
    row, col = divmod(i, 2)
    c = ax[row, col].imshow(eof, cmap="coolwarm", aspect="auto")
    fig.colorbar(c, ax=ax[row, col])
    ax[row, col].set_title(f"EOF{i+1} (Cloud Cover)")

for j in range(5, 6):
    fig.delaxes(ax.flatten()[j])

plt.tight_layout()
plt.show()


# In[ ]:




