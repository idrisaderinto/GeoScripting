import osmnx as ox
import geopandas as gpd
import pandas as pd

## First function that create the area of classes Building, Paved, Water, Green using footprint modules
def GetOSMdata(placename='University of Lagos', EPSGcode='28992'):
    """This function uses the OSMNX package to extract a geometry 
    representing the placename provided as input and transforms to 
    the required projection (EPSG code)"""
    
    CampusGDF = ox.gdf_from_place(placename)
    CampusGDF = ox.project_gdf(CampusGDF, to_latlong = True)
    bboxUniversity_Lagos = list(CampusGDF.total_bounds)
    xmin, ymin, xmax, ymax = bboxWageningen
    
    BuildingsGDF = ox.footprints.create_footprints_gdf(polygon=CampusGDF, west=xmin, south=ymin, east=xmax, north=ymax, footprint_type='building')
    BuildingsGDF = gpd.overlay(CampusGDF, BuildingsGDF, how='intersection')
    
    PavedGDF = ox.footprints.create_footprints_gdf(polygon=CampusGDF, west=xmin, south=ymin, east=xmax, north=ymax, footprint_type='highway')
    PavedGDF = gpd.overlay(PavedGDF, BuildingsGDF,  how="difference")
    
    WaterGDF = ox.footprints.create_footprints_gdf(polygon=CampusGDF, west=xmin, south=ymin, east=xmax, north=ymax, footprint_type='water')
    WaterGDF = gpd.overlay(WaterGDF, PavedGDF,  how="difference")
    
    GreenGDF = ox.footprints.create_footprints_gdf(polygon = CampusGDF, north=ymax, south=ymin, east=xmax, west=xmin, footprint_type='natural')  
    GreenGDF = gpd.overlay(GreenGDF, CampusGDF, how="intersection")  
    
    CampusGDF = ox.projection.project_gdf(CampusGDF)
    BuildingsGDF = ox.projection.project_gdf(BuildingsGDF)
    PavedGDF = ox.projection.project_gdf(PavedGDF)
    WaterGDF = ox.projection.project_gdf(WaterGDF)
    GreenGDF = ox.projection.project_gdf(GreenGDF)

    return CampusGDF, BuildingsGDF, PavedGDF, WaterGDF, GreenGDF

# Second function that create a standardized topographical map
def CreateCampusMap(BuildingsGDF, PavedGDF, WaterGDF, GreenGDF): 
    """"
    The function takes in given OSMdata and 
    creates a topographical map using matplotlib
    """
    
    import matplotlib.pyplot as plt
    
    figure, ax = plt.subplots(figsize=(10,10))
    BuildingsGDF.plot(ax=ax, color='brown')
    PavedGDF.plot(ax=ax, color='yellow', edgecolor='black', label='paved areas')
    WaterGDF.plot(ax=ax, color='blue', label='water')
    GreenGDF.plot(ax=ax, color='green', label='green areas')
    plt.title("Campus Map", fontsize=16)
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
    plt.show()
    
    
#Third function that reprojectiong the GeDataFrame to the required projection
def reproject(GDF, CRScode):
    """
    This function takes in a GeoDataFrame and a CRS Code as arguments and 
        returns a reprojected GeoDataFrame
    """
    import osmnx.projection
    GDF = osmnx.projection.project_gdf(GDF, to_crs = CRScode)
    return GDF


 #Fourth function that visualize the subscores for a certain campus nicely in a radar chart
def CreateScoreRadarOverview(CampusGDF,BuildingsGDF, PavedGDF, WaterGDF, GreenGDF):
   """
   a function that, taking a pandas dataframe as input, 
   visualizes the subscores for a certain campus nicely in a radar chart.
   """
   
    # Libraries
   import geopandas as gpd
   import matplotlib.pyplot as plt
   import pandas as pd
   from math import pi
    
    #Sum up and claculate the percentage area
   CampusArea = sum(CampusGDF.area)
   BuildingsArea = sum(BuildingsGDF.area)
   PavedArea = sum(PavedGDF.area)
   WaterArea = sum(WaterGDF.area)
   GreenArea = sum(GreenGDF.area)
    
   PercentageBuildingsCoverage = (BuildingsArea/CampusArea)*100    
   PercentagePavedCoverage = (PavedArea/CampusArea)*100
   PercentageWaterCoverage = (WaterArea/CampusArea)*100
   PercentageGreenCoverage = (GreenArea/CampusArea)*100
   PercentageOtherCoverage = 100 - (PercentageBuildingsCoverage+PercentagePavedCoverage+PercentageWaterCoverage+PercentageGreenCoverage)

    # Set data as GeoDataFrame
   df = pd.DataFrame({
        'group': ['Coverage'],
        'Buildings': [PercentageBuildingsCoverage],
        'Paved': [PercentagePavedCoverage],
        'Water': [PercentageWaterCoverage],
        'Green': [PercentageGreenCoverage],
        'Other': [PercentageOtherCoverage]
        })

    # number of variable
   categories=list(df)[1:]
   N = len(categories)

    # Plot the first line of the data frame
   values=df.loc[0].drop('group').values.flatten().tolist()
   values += values[:1]
   values

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
   angles = [n / float(N) * 2 * pi for n in range(N)]
   angles += angles[:1]

    # Initialise the spider plot
   ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels labels yet
   plt.xticks(angles[:-1], categories, color='grey', size=8)

    # Draw ylabels
   ax.set_rlabel_position(0)
   plt.yticks([10,20,30], ["10","20","30"], color="grey", size=7)
   plt.ylim(0,40)

    # Plot data
   ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
   ax.fill(angles, values, 'b', alpha=0.1)    
   plt.show() 
    
