Alphabetical list of ArcPy functions: https://euclgis.reg.rw/portal/portalhelp/en/notebook/latest/python/windows/alphabetical-list-of-arcpy-functions.htm

CON: 
https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/con-.htm
https://gis.stackexchange.com/questions/39139/making-new-raster-using-con-script-using-arcpy
https://gis.stackexchange.com/questions/261252/arcgis-raster-calculator-con-statement?rq=1
https://resources.arcgis.com/en/help/main/10.1/index.html#//009z000000zn000000
    
What is the Raster Cell Iterator? read, write to cells
https://pro.arcgis.com/en/pro-app/latest/help/analysis/spatial-analyst/raster-cell-iterator/what-is-the-raster-cell-iterator.htm
https://pro.arcgis.com/en/pro-app/latest/help/analysis/spatial-analyst/raster-cell-iterator/a-quick-tour-of-using-the-raster-cell-iterator.htm
      
Introducing the Raster Cell Iterator https://www.esri.com/arcgis-blog/products/spatial-analyst/analytics/introducing-the-raster-cell-iterator/
  
Get Raster Properties (Data Management) https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/get-raster-properties.htm
    
copy, delete raster: https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/copy.htm
    
Raster mergen und Con(): https://pro.arcgis.com/en/pro-app/latest/help/analysis/spatial-analyst/mapalgebra/building-complex-statements.htm
Raster modifien und abspeichern, for: https://support.esri.com/en/technical-article/000022418
Additional ArcGIS Pro Functions: https://gsp.humboldt.edu/olm/Courses/GSP_318/05_4_1_RasterArithmatic.html
    
raster, numpy, loop, cells of raster, path, save How to calculate the mean value of multiple large rasters in python/arcpy?: https://stackoverflow.com/questions/72655982/how-to-calculate-the-mean-value-of-multiple-large-rasters-in-python-arcpy
RasterToNumPyArray: https://euclgis.reg.rw/portal/portalhelp/en/notebook/latest/python/windows/rastertonumpyarray-function.htm

numpy, copyRaster: https://gist.github.com/kevin-peel/e47738b6afba31f5419c
Raster Compare: https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/raster-compare.htm
map algebra on raster: https://www.e-education.psu.edu/geog485/node/311
    
SINNVOLLE FOLIEN MIT CODE SNIPPETS zu Rastern: https://here.isnew.info/accessing-raster-data-using-arcpy.html#/-save-raster

Raster, loop, while: https://community.esri.com/t5/python-questions/raster-calculator-within-loop/td-p/558106
with/reset resource in loop: https://gis.stackexchange.com/questions/74325/arcpy-nested-loop-problem
    
loop, folder, path, con, save: https://gis.stackexchange.com/questions/332925/looping-through-two-raster-folders-to-perform-raster-calculation

WICHTIG Raster (Grid) Handling: https://hydro-informatics.com/jupyter/geo-raster.html
https://desktop.arcgis.com/en/arcmap/10.3/analyze/arcpy-classes/raster-object.htm
https://pro.arcgis.com/en/pro-app/latest/arcpy/classes/raster-object.htm

noData:
    https://gis.stackexchange.com/questions/282073/set-raster-properties-in-arcpy-multiple-no-data-values-for-single-band-raster
    https://support.esri.com/en/technical-article/000010059
    

path:https://community.esri.com/t5/python-questions/error-999998-unexpected-error-raster-algebra/td-p/392130
 for inraster in rasterlist:
    print inraster
    tx_name = os.path.join(OUTFOLDER, str(inraster))

arcpy.env.overwriteOutput=True
if arcpy.Exists(outName):
        arcpy.Delete_management(outName)‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍

