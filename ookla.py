from datetime import datetime

import geopandas as gp
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from shapely.geometry import Point
from adjustText import adjust_text

# Reading downloaded file from Ookla's AWS Repository
tile_url = "2020-04-01_performance_fixed_tiles.zip"
tiles = gp.read_file(tile_url)

# Creating dataframe to write csv file
tiles_df = pd.DataFrame(tiles, copy=True)
tiles.to_csv('tiles_df.csv')


# zipfile of U.S. counties
county_url = "https://www2.census.gov/geo/tiger/TIGER2019/COUNTY/tl_2019_us_county.zip" 
counties = gp.read_file(county_url)

# Filtering counties to add to crs and dataframe to create csv file
all_counties = counties.to_crs(4326)
counties_df = pd.DataFrame(all_counties, copy= True)
counties_df.to_csv('counties.csv')

# Creating inner join on tiles of counties using geopandas
tiles_counties = gp.sjoin(tiles, all_counties, how="inner", op='intersects')

# creating dataframe from counties tiles to write csv file
all_df = pd.DataFrame(tiles_counties, copy= True)
all_df.to_csv('all_data.csv')


