#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# For setting up a correct 'geoscripting' conda env (if you don't yet have:) run in terminal:
#   conda create --name geoscripting --file https://raw.githubusercontent.com/geoscripting-2020/Exercise10_solution/master/SetUpCondaEnv.txt?token=AK6V4SJOBDUDL2YBSJ4EJNK556L2M
#   pip install fiona==1.8.8 geopandas rasterio rasterstats
"""
import os
if not os.path.exists('data'): os.makedirs('data')
if not os.path.exists('output'): os.makedirs('output')
# import my own developed functions
import MyFunctions_VectorExc as funcs

# extract the AOI(Area of Interest) geometry from OSM, the placename should replace 'AOI'
PlaceGDF = funcs.GeocodePlacenameToGDF('AOI', '28992')
print(PlaceGDF)

# extract extent from the AOI geometry
bboxAOI = list(PlaceGDF.total_bounds)
print(bboxAOI)

# extract buildings geometries for the AOI
BuildingsGDF = funcs.BAGtoGeoDataFrame(bbox=bboxAOI)
print(BuildingsGDF)

# perform spatial overlay and calculate overlap area in %
AOIbuildingsGDF, BuildingsArea, PercentageCoverage = funcs.CalculatePercentageArea(DomainGDF=PlaceGDF, ObjectGDF=BuildingsGDF)

# print a nice summary
print("The AOI has a total surface area of "
          + str(round(sum(PlaceGDF.area)/10000, 2)) + " ha. Within this domain, the buildings cover a total of "
          + str(round(PercentageCoverage, 1)) + "% of the domain surface area.")

# visualize the AOI and buildings within it
import folium
AOIbuildingsGDF = AOIbuildingsGDF.to_crs({'init': 'epsg:4326'})
PlaceGDF = PlaceGDF.to_crs({'init': 'epsg:4326'})
xcoord, ycoord = PlaceGDF.centroid.x, PlaceGDF.centroid.y
AOIMap = folium.Map([ycoord, xcoord], zoom_start=16)
AOIMap.choropleth(PlaceGDF, name="AOI Campus")
AOIMap.choropleth(AOIbuildingsGDF, name="Buildings", fill_color='red')
folium.LayerControl().add_to(AOIMap)
AOIMap.save('./output/campusMap.html')

