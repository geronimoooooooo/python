import rasterio

#dataset= rasterio.open('C:\\rasta\\foc2.tif') C:\rasta\final
dataset= rasterio.open('C:\\rasta\\final\\zonM.tif') 
print('dataset.width: '+ str(dataset.width))
#print(dataset.indexes)


band1 = dataset.read(1)
#print(band1[1300,1300])

for row in range(1000,dataset.width, 3):    
	if band1[1000,row] > 0:
		print("row: "+ str(row))
		print(band1[1000,row])
		#print(row)