import rasterio
from rasterio.plot import show, show_hist




ds = rasterio.open('nepal.tif')
print(ds.shape)
print(ds.indexes)
print(ds.count)
#show(ds)
#show(ds,cmap='summer', title="Salzburg")
#show_hist(ds,bins=50, title="Histogram Salzburg")
data = ds.read(1)
print(ds.read().size)
print(ds.meta)
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
