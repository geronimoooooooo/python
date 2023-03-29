
How to sort dictionary by key or value in numerical order Python
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
                 
    #if raster_sum cell value > XX; True: write new value from raster_mean; False: write NoData
    # smaller cluster disapear
    raster_out_sum_mean = Int(Con(raster_sum > init_file.cluster_threshold_final, raster_mean))

--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------


