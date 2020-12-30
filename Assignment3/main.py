# Importing module with functions
import MyFunctions_3 as myFunc

# Importing packages
import osmnx as ox
import osmnx.projection
import os
import pandas as pd

# Creating data and output folders
if not os.path.exists('data'): os.makedirs('data')
if not os.path.exists('output'): os.makedirs('output')

# Calling the function that extracts osm data and returns the GeoDataFrame
(CampusGDF, BuildingsGDF, PavedGDF, WaterGDF, GreenGDF) = myFunc.GetOSMdata('University of Lagos')

# Reprojecting the data to the appropriate CRS
RDcode = '+init=epsg:28992'  
CampusGDF = myFunc.reproject(CampusGDF, RDcode)
BuildingsGDF = myFunc.reproject(BuildingsGDF, RDcode)
PavedGDF = myFunc.reproject(PavedGDF, RDcode)
WaterGDF = myFunc.reproject(WaterGDF, RDcode)
GreenGDF =myFunc.reproject(GreenGDF, RDcode)

# Plotting the OSMdata to create a standardized topographical map
CampusMap = myFunc.CreateCampusMap(BuildingsGDF, PavedGDF, WaterGDF, GreenGDF)
CampusMap

# View Score Radar Overview 
radarOverview = myFunc.CreateScoreRadarOverview(CampusGDF,BuildingsGDF, PavedGDF, WaterGDF, GreenGDF)
radarOverview