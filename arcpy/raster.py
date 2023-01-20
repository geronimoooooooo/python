What is the Raster Cell Iterator? https://pro.arcgis.com/en/pro-app/latest/help/analysis/spatial-analyst/raster-cell-iterator/what-is-the-raster-cell-iterator.htm
Introducing the Raster Cell Iterator https://www.esri.com/arcgis-blog/products/spatial-analyst/analytics/introducing-the-raster-cell-iterator/
  
  Get Raster Properties (Data Management) https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/get-raster-properties.htm
    
    
Raster mergen und Con(): https://pro.arcgis.com/en/pro-app/latest/help/analysis/spatial-analyst/mapalgebra/building-complex-statements.htm
Raster modifien und abspeichern, for: https://support.esri.com/en/technical-article/000022418
Additional ArcGIS Pro Functions: https://gsp.humboldt.edu/olm/Courses/GSP_318/05_4_1_RasterArithmatic.html
    
raster, numpy, loop, cells of raster, path, save How to calculate the mean value of multiple large rasters in python/arcpy?: https://stackoverflow.com/questions/72655982/how-to-calculate-the-mean-value-of-multiple-large-rasters-in-python-arcpy

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

path:https://community.esri.com/t5/python-questions/error-999998-unexpected-error-raster-algebra/td-p/392130
 for inraster in rasterlist:
    print inraster
    tx_name = os.path.join(OUTFOLDER, str(inraster))

arcpy.env.overwriteOutput=True
if arcpy.Exists(outName):
        arcpy.Delete_management(outName)‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍‍


