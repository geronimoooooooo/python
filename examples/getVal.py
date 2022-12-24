# https://gis.stackexchange.com/questions/358036/extracting-data-from-a-raster/358058#358058

import rasterio
from pyproj import Transformer

lon = 15.174866
lat = 43.169129

with rasterio.open("C:/path-to-the-map/map.tif") as rds:
    # convert coordinate to raster projection
    transformer = Transformer.from_crs("EPSG:4326", rds.crs, always_xy=True)
    xx, yy = transformer.transform(lon, lat)

    # get value from grid
    value = list(rds.sample([(xx, yy)]))[0]
    