{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Example\n",
    "import datetime\n",
    "\n",
    "bounding_box = {'max_lat':65, 'min_lat':60, 'max_lon':-167, 'min_lon':-172}\n",
    "\n",
    "estimated_breakup_date = datetime.datetime(2000, 3, 15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "metadata": {},
   "outputs": [],
   "source": [
    "import xarray as xr\n",
    "import datetime\n",
    "\n",
    "def mean_30d_raster_temps(bounding_box,estimated_breakup_date):\n",
    "    start_date = estimated_breakup_date - datetime.timedelta(days=30) #30 days or 31 days in total?\n",
    "    end_date = estimated_breakup_date\n",
    "\n",
    "    fp = f'/home/jovyan/work/ESDA_hk339/Project/daily_temps.nc'\n",
    "    ds = xr.open_dataset(fp)\n",
    "    \n",
    "    #ds.load()\n",
    "\n",
    "    temp = ds['TMP_DAILY'] - 273.15#.values\n",
    "    temp_30d = temp.sel(time=slice(start_date, end_date))\n",
    "    \n",
    "    min_lon = bounding_box['min_lon'] + 360\n",
    "    max_lon = bounding_box['max_lon'] + 360\n",
    "    \n",
    "    temp_bbox = temp_30d.sel(\n",
    "        lat=slice(bounding_box['max_lat'], bounding_box['min_lat']),  #Latitudes go from max to min\n",
    "        lon=slice(min_lon, max_lon)\n",
    "    )\n",
    "    \n",
    "    mean_30d_temp = temp_bbox.mean().item()\n",
    "    \n",
    "    return mean_30d_temp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-8.069668769836426\n"
     ]
    }
   ],
   "source": [
    "mean_30d_temp = mean_30d_raster_temps(bounding_box,estimated_breakup_date)\n",
    "print(mean_30d_temp)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 205,
   "metadata": {},
   "outputs": [],
   "source": [
    "def monthly_raster_temps(bounding_box):\n",
    "    fp = f'/home/jovyan/work/ESDA_hk339/Project/monthly_temps.nc'\n",
    "    ds = xr.open_dataset(fp)\n",
    "    \n",
    "    ds.load()\n",
    "    \n",
    "    temp = ds['TMP_DAILY']-273.15\n",
    "    lat = ds['lat']#.values\n",
    "    lon = ds['lon']#.values\n",
    "    time = ds['time']#.values\n",
    "      \n",
    "    lat_condition = (lat >= bounding_box['min_lat']) & (lat <= bounding_box['max_lat'])\n",
    "    lon_condition = (lon >= bounding_box['min_lon']+360) & (lon <= bounding_box['max_lon']+360) #Convert lon to 0-360\n",
    "\n",
    "    extracted_temp = temp.sel(lat=lat[lat_condition], lon=lon[lon_condition])\n",
    "    \n",
    "    monthly_temp = extracted_temp.mean(dim=('lat', 'lon'))\n",
    "    \n",
    "    return monthly_temp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "metadata": {},
   "outputs": [],
   "source": [
    "monthly_temp = monthly_raster_temps(bounding_box)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
