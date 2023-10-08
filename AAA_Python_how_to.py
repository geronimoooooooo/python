viele how to in python https://note.nkmk.me/en/python/
-------------------------------------------------------------------------------------------

DICTIONARY
Python | Get dictionary keys as a list https://www.geeksforgeeks.org/python-get-dictionary-keys-as-a-list/
How to create list of dictionary in Python https://www.geeksforgeeks.org/python-extract-specific-keys-from-dictionary/?ref=ml_lbp
How to create list of dictionary in Python https://www.geeksforgeeks.org/how-to-create-list-of-dictionary-in-python/
https://www.scaler.com/topics/list-of-dictionaries-in-python/
iterate .keys(), .items(), .values() https://note.nkmk.me/en/python-dict-keys-values-items/

https://www.geeksforgeeks.org/how-to-use-dict-get-with-multidimensional-dict/
https://www.freecodecamp.org/news/python-sort-dictionary-by-key/
--------------------------------------------------------------------------------------------------------  
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

--------------------------------------------------------------------------------------------------------
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
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
# Mosaic temporary files
arcpy.Mosaic_management(';'.join(filelist[1:]), filelist[0])

--------------------------------------------------------------------------------------------------------
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
--------------------------------------------------------------------------------------------------------


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
Raster path
with arcpy.EnvManager(workspace = wks):
	list_raster = arcpy.ListRasters("*", "GRID")     
	list_raster_obj = [Raster(ras) for ras in list_raster]
	list_raster_obj2 = [Raster(os.path.join(wks, ras)) for ras in list_raster] 
	list_raster_obj_path = [Raster(arcpy.Describe(ras).catalogPath) for ras in list_raster]

	logger.debug(f'Raster in arcpy.env.workspace: {arcpy.env.workspace}')
	for index, ras in enumerate(list_raster,1):
			print(f' {index}. {ras}')
			#1. r_200	
	for index, ras in enumerate(list_raster_obj,1):
      logger.info(f' {index}. {ras.name} {ras} {ras.catalogPath}')
			# 1. r_200 r_200 C:\Users\slukic\Documents\ArcGIS\Projects\MyProject2\Skeleton_raster.gdb\r_200

  for index, ras in enumerate(list_raster_obj2,1):
      logger.info(f' {index}. {ras.name} {ras} {ras.catalogPath}') 
		  1. r_200 C:\Users\slukic\Documents\ArcGIS\Projects\MyProject2\Skeleton_raster.gdb\r_200 C:\Users\slukic\Documents\ArcGIS\Projects\MyProject2\Skeleton_raster.gdb\r_200
	
	for index, ras in enumerate(list_raster_obj_path,1):
      logger.info(f' {index}. {ras.name} {ras} {ras.catalogPath}')  
			#1. r_200 C:\Users\slukic\Documents\ArcGIS\Projects\MyProject2\Skeleton_raster.gdb\r_200 C:\Users\slukic\Documents\ArcGIS\Projects\MyProject2\Skeleton_raster.gdb\r_200

        # list_raster_obj = [Raster(arcpy.Describe(ras).catalogPath) for ras in list_raster] #p(el)==path
        list_raster_obj = [Raster(ras) for ras in list_raster] #p(el)==filename
        for r in list_raster:
            ras = Raster(r)
            print((ras.catalogPath))
            list_raster_obj.append(ras)
			
--------------------------------------------------------------------------------------------------------
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

# Process: Build Raster Attribute Table (Build Raster Attribute Table) (management)
# amodelmos_last11_3_ = arcpy.management.BuildRasterAttributeTable(in_raster=arcpy_first22, overwrite="Overwrite", convert_colormap="NONE")[0]
--------------------------------------------------------------------------------------------------------
raster_t2_name = os.path.splitext(os.path.basename(init_file.merged_raster_t2))[0]
print(raster_t2_name, init_file.merged_raster_t2 )
# arc_rc_final_T2 C:\Users\slukic\Documents\ArcGIS\Projects\MyProject2\Result_raster.gdb\arc_rc_final_T2
--------------------------------------------------------------------------------------------------------
def create_filler_raster_metadata(dict_ras_skeleton_metadata:dict[int,list])->dict[int,list]:
--------------------------------------------------------------------------------------------------------
# helper_functions.sort_reverse_list(list_raster_obj_complete)
#     dicta_sorted = {k: dicta[k] for k in sorted(dicta, key= raster_query.natkey)}
# dicta_sorted_reversed = dict(reversed(dicta_sorted.items()))
--------------------------------------------------------------------------------------------------------
os.path.basename(arcpy.env.workspace)  # liefert vom pfad nur letzten Teil mit: used.gdb
raster_t2_name = os.path.splitext(os.path.basename(init_file.merged_raster_t2_path))[0] # liefert Dateiname ohne Extension
--------------------------------------------------------------------------------------------------------
for index, file in enumerate(list_raster, 1):
    #get the threshold number from file name
    threshold = int(file.split("_")[-1]) #r_200 wird zu = 200
--------------------------------------------------------------------------------------------------------
 list_ras_skeleton = list(dict_ras_skeleton_metadata.keys())
dict_ras_filler_metadata_local = {}
ras_minus_1 = list_ras_skeleton[0]    
dict_ras_skeleton_metadata[ras_minus_1][2] = 0 #set relative % diff to the skeleton raster before itself
for ras in list_ras_skeleton[1:]:     
--------------------------------------------------------------------------------------------------------
for i in range(8)[::2]:
    print(i)
--------------------------------------------------------------------------------------------------------
lisa_obj.sort(key=lambda obj: helper_functions.natkey(obj.name))
    dicta_sorted = {k: dicta[k] for k in sorted(dicta, key= helper_functions.natkey)}
    dicta_sorted_reversed = dict(reversed(dicta_sorted.items()))

--------------------------------------------------------------------------------------------------------
lisa_ohne_r.append(int(ras.split('_')[-1]))
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
