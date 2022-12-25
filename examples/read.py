import rasterio
from rasterio.plot import show, show_hist
from rasterio import DatasetReader
import rioxarray



ds = rasterio.open('nepal.tif')
x ="ab"


print(ds.shape)
print(ds.indexes)
print(ds.count)
print("nodata is: "+ str(ds.nodata))
#show(ds)
#show(ds,cmap='summer', title="Salzburg")
#show_hist(ds,bins=50, title="Histogram Salzburg")
data = ds.read(1)
print(ds.read().size)
print(ds.meta)
print("resolution" + str(ds.res))
print(data.size)
print(data.min())
print(data.max())


print(data)
data[1,1]=1

for row in range(500,900):
    for col in range(500,600):
        data[row,col] = 170

for row in range(1,600):    
    pass
    #data[row,row]=100
    #print(row)

print(data)

#complete example to create .tif https://pypi.org/project/rasterio/1.3.3/#description
#https://stackoverflow.com/questions/58193526/rasterio-source-shape-is-inconsistent-with-given-indexes-1
#https://rasterio.readthedocs.io/en/latest/topics/writing.html
#https://gis.stackexchange.com/questions/279953/numpy-array-to-gtiff-using-rasterio-without-source-raster

#öffnet einige files mit rioxarray und rasterio.open https://www.youtube.com/watch?v=TbbL2yeRTsk
#check for nodata values https://www.youtube.com/watch?v=SCHTZ4oaohA
#MEHRERE .tif files werden in array eingelesen und abgearbeitet 
# Reading And Plotting Raster Data With Rioxarray https://adenaheem.com/reading-and-plotting-raster-data-with-rioxarray/
# MMerge rasters in Python using Rioxarray https://spatial-dev.guru/2022/09/29/merge-rasters-in-python-using-rioxarray/
# Getting pixel values at single point using rasterio https://gis.stackexchange.com/questions/190423/getting-pixel-values-at-single-point-using-rasterio

with rasterio.open(r"nepal_out3.tif", 'w',
                    driver=ds.driver,
                    height=ds.height,
                    width=ds.width,
                    count=ds.count,
                    crs=ds.crs,
                    transform=ds.transform,
                    dtype=data.dtype,
                    compress='lzw'                
                ) as dst:
    dst.write(data, indexes=1)

dsNepal = rasterio.open("nepal_out3.tif")
show(dsNepal, cmap="rainbow")


rioData = rioxarray.open_rasterio('nepal.tif')

print(rioData.rio.bounds())
print("reso: ",rioData.rio.resolution())

print("raster value on point %.6f" %ds.read(1)[199,100]) #row,col
