import rasterio
import numpy as np
import matplotlib
from rasterio.transform import from_origin
from rasterio.plot import show 

arr = np.random.randint(5, size = (100, 100))
#arr = np.random.randint(5, size=(100,100)).astype(np.float)

transform = from_origin(472137, 5015782, 0.5, 0.5)

new_dataset = rasterio.open('test1.tif', 'w', driver='GTiff',
                            height = arr.shape[0], width = arr.shape[1],
                            count=1, dtype=str(arr.dtype),
                            crs='+proj=utm +zone=10 +ellps=GRS80 +datum=NAD83 +units=m +no_defs',
                            transform=transform)

new_dataset.write(arr, 1)
new_dataset.close()

print(new_dataset.name)
print(new_dataset.count)
print(new_dataset.shape)

data = rasterio.open('water.tif')
print(data.indexes)
band1 = data.read(1)

print(band1)


#show(band1)

for col in range(3, data.width,3):
    pass
    #print(str(col)+", "+str(band1[col,2]))