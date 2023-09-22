
How to sort dictionary by key or value in numerical order Python
https://realpython.com/iterate-through-dictionary-python/#sorted-by-keys
https://realpython.com/sort-python-dictionary/
https://stackoverflow.com/questions/22264956/how-to-sort-dictionary-by-key-in-numerical-order-python
https://stackoverflow.com/questions/9001509/how-do-i-sort-a-dictionary-by-key
https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
--------------------------------------------------------------------------------------------------------  
Merge 2 dict
https://www.digitalocean.com/community/tutorials/python-add-to-dictionary#adding-to-a-dictionary-using-the-merge-operator
--------------------------------------------------------------------------------------------------------
Reverse list
https://www.programiz.com/python-programming/methods/list/reverse
--------------------------------------------------------------------------------------------------------
zip 2 Listen
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')
    
for el in zip(names,ages):
    name, age = el
    print(f'{name} is {age}')
    
# Assign values to initialized dictionary keys. Using dict() + zip()
res = dict(zip(test_dict, test_list))

for key, val in zip(test_dict, test_list):
    test_dict[key] = val
--------------------------------------------------------------------------------------------------------
Stacktrace caller functions
https://stackoverflow.com/questions/5067604/determine-function-name-from-within-that-function-without-using-traceback
--------------------------------------------------------------------------------------------------------
Slicing
https://stackoverflow.com/questions/509211/understanding-slicing
https://stackoverflow.com/questions/10623302/how-does-assignment-work-with-list-slices
--------------------------------------------------------------------------------------------------------
create folder if it does not exist
import os, os.path
if not os.path.exists("qe/logs/"):
    os.makedirs("qe/logs/")
--------------------------------------------------------------------------------------------------------
import sys
from pprint import pprint
    pprint(sys.path) #print all paths
    
import importlib.util    
    print(importlib.util.find_spec("arcpy").origin) #print path of a module
--------------------------------------------------------------------------------------------------------
Split a List Into Evenly Sized Chunks
https://realpython.com/how-to-split-a-python-list-into-chunks/
https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
https://www.programiz.com/python-programming/examples/list-chunks
--------------------------------------------------------------------------------------------------------
repeat last element of list
https://stackoverflow.com/questions/63655242/whats-the-pythonic-way-to-repeat-first-and-last-element-of-a-list
--------------------------------------------------------------------------------------------------------
nums = [1,3,4,6,11]
t = 9

for n in nums:
    if (t-n) in nums:
        print(f'found {n} and {t-n}')
--------------------------------------------------------------------------------------------------------
os.path.basename(arcpy.env.workspace} #liefert alles nach dem letzten '\' some_folder.gdb
--------------------------------------------------------------------------------------------------------
 CON: https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/con-.htm
    ras1 = list_ras_obj[0]
    # check at raster ras1 each cell if val==0
    # if true, set noData else remain ras1 values
    rasa = SetNull(ras1==0,ras1)
    rasa.save(path_to_raster+"_rasa")

    ras2 = list_ras_obj[0]
    # check at raster ras2 each cell if val==0
    # if true, set noData else remain ras2 values
    rasb = SetNull(ras2, ras2, "VALUE=0")
    rasb.save(path_to_raster+"rasb")

    # Schallpegel von >70 dB auf NULL setzten um Rastergröße einzuschränken
    out_rast2 = SetNull(out_rast1,out_rast1,"value > 70")
                 
    #if raster_sum cell value > XX; True: write new value from raster_mean; False: write NoData
    # smaller cluster disapear
    raster_out_sum_mean = Int(Con(raster_sum > init_file.cluster_threshold_final, raster_mean))

--------------------------------------------------------------------------------------------------------
write to file
f = open(dir +"\\file.txt", "w")
someText= ("a: "+ a +"\n"+"b: "+b)
f.write(someText)
f.close()
--------------------------------------------------------------------------------------------------------
Argumente an Skript übergeben: 
https://www.geeksforgeeks.org/command-line-arguments-in-python/
https://www.knowledgehut.com/blog/programming/sys-argv-python-examples
with...
for arg in sys.argv:
  print(arg)
--------------------------------------------------------------------------------------------------------
how to log only one level
import logging, sys

class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        print(f"{logRecord}rec", logRecord.levelno)
       # print(self.__level)
        return logRecord.levelno > self.__level

#create a logger
logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)
#handler = logging.FileHandler('mylog.log')
handler = logging.StreamHandler(stream=sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
#set filter to log only INFO lines
handler.addFilter(MyFilter(logging.INFO))
logger.addHandler(handler)

#write an INFO line to log file
logger.info('This is a INFO message') #20
logger.warning('This is a WARNING message') #30
logger.error('This is an ERROR message') #40
logger.critical('This is a CRITICAL message') #50
--------------------------------------------------------------------------------------------------------
def args_kwargs(*args,c=10,**kwargs):
    print("args:", args) # args: (1, 22, 33, 44)
    print("c:", c) # c: 10
    print("kwargs:", kwargs) # kwargs: {'k1': 8, 'k2': 9}
    
args_kwargs(1,22,33,44, k1=8, k2=9)
--------------------------------------------------------------------------------------------------------
print(pi) # 3.14159
print(int(pi)) # 3
print(round(pi,4)) # 3.1416
print(int((pi*10000))) # 31415
print((pi*10000)//1) # 31415.0
--------------------------------------------------------------------------------------------------------
'%0.2f'  %(0.123455)
 f'{someFloat:0.2f}'
--------------------------------------------------------------------------------------------------------
for row in arcpy.SearchCursor(myTable)
	print(row.getValue("col")	
				 
--------------------------------------------------------------------------------------------------------
inras = "ras100" 
# convert raster to Numnpy array 
rasArray = arcpy.RasterToNumPyArray(inras) 

# ARRAY SLICING: get the total sum of every third value 
# from every third row of the raster 
sampArray = rasArray[::3,::3] 
sum = numpy.sum(sampArray) 
print sum
--------------------------------------------------------------------------------------------------------
# create dir
os.makedir(path)

#create new file geodatabase
arcpy.CreateFileGDB_management(path_folder, "abc.gdb")

lisa = arcpy.ListRaster()
for ras in lisa:
   arcpy.
--------------------------------------------------------------------------------------------------------
if os.path.isdir(‘C:/Some/Path’):
# os.listdir gives a list of everything in a specific folder.
dir_list = os.listdir(input_folder)
--------------------------------------------------------------------------------------------------------
# Mosaic temporary files
arcpy.Mosaic_management(';'.join(filelist[1:]), filelist[0])
if arcpy.Exists(fileout):
    arcpy.Delete_management(fileout)
arcpy.Rename_management(filelist[0], fileout)
--------------------------------------------------------------------------------------------------------
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
--------------------------------------------------------------------------------------------------------
list_names =["a","b"]
#dict comprehension
dict_names = {name:len(name) for name in list_names}
--------------------------------------------------------------------------------------------------------
lisa = [1,2,3]
lisb = [11,22,33]
lisc = [111,222,333]
for i,(a,b,c) in enumerate(zip(lisa,lisb,lisc)):
	print(a,b,c,sep="--")
--------------------------------------------------------------------------------------------------------
filtered = filter(func, lista)
filtered = (el for el in lista if func(el)) #generator comprehensions
	      
mapped = map(func, lista)
mapped = (func(el) for el in lista)
--------------------------------------------------------------------------------------------------------
IMMER NUTZEN

def main():
	dostuff()

if __name__=='__main__':
	main()
--------------------------------------------------------------------------------------------------------
filein = os.path.join(os.getcwd(), r"input\input.tif") #folder where command line is executed
OutTIFFname = "{}_{}_kd.tif".format(os.path.splitext(fc)[0],FieldValue)
isFile = os.path.isfile(path)
exists = os.path.exists(rasterOutputFolder)
files = [os.path.join(arcpy.env.workspace, r) for r in files]

outras = Con(IsNull(ras100), val, ras100) #checks for NoData
--------------------------------------------------------------------------------------------------------
importieren von libraries aus anderen foldern https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
