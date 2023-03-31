

import pandas as pd
import geopandas as gpd
import os
import glob
import wget

root_path = os.path.abspath('..')

gdf = gpd.read_file(os.path.join(root_path, "datasets/NAIP_overlap.shp"))
output_dir = os.path.join(root_path, 'datasets/image_tiles')

all_links = gdf['URL'].tolist()
all_names = gdf['location'].tolist()


download = False
while download:
    download = False
    for link, name in zip(all_links, all_names):

        if not os.path.isfile(os.path.join(output_dir, name)):
            wget.download(link, os.path.join(output_dir, name))




