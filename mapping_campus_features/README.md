## Mapping Campus Features
This project aims to map 5 campus features (Building, Paved, Water, Green, Other) by utilizing data from OpenStreetMap. Mapping campus features gives an idea of land cover and how much green is present within a campus.

### Details
* The folder works with a project structure and well-structured scripts were created with one main script. A main.py module was made that imports functions from another Python module called 'MyFunctions_3.py'. 
* The OpenStreetMap data was utilized. The OSMNX package developed by [Geoff Boeing](https://geoffboeing.com/), was employed and the documentation can be found here; [osmnx documentation](https://osmnx.readthedocs.io/en/stable/osmnx.html). Also, the [footprints module](https://osmnx.readthedocs.io/en/stable/osmnx.html#module-osmnx.footprints) that allows the easy extraction of footprints (for example landuse or buildup) from OpenStreetMap was utilized.

### Processes
1. The percentage coverage of: Buildings, paved, water, green and other areas were calculated.
      * Footprint data from OSM does sometimes overlap with each other. It was ensured the 5 classes together added up to 100%. For this the following priority order was taken into account  (from most important to less): Building -> Paved -> Water -> Green -> Other
2. The functions should download the required geodata (no manual download)
3. For this project the following functions were created:
    * <u>Required</u>: <b>GetOSMdata</b> a function that, for a given placename, extracts OSM data and returns these as GeoDataFrames. It returns back:
          a. <b><i>CampusGDF</i></b> a GeoDataFrame with just one record containing the campus area polygon
          b. <b><i>BuildingsGDF</i></b> a GeoDataFrame with all buildings within the campus area
          c. <b><i>PavedGDF</i></b> a GeoDataFrame with geometries representing paved areas
          d. <b><i>WaterGDF</i></b> a GeoDataFrame with geometries representing open water bodies 
          e. <b><i>GreenGDF</i></b> a GeoDataFrame with geometries representing green areas
    * <u>Required</u>: <b>CreateCampusMap</b> a function that, given the OSMdata, creates a standardized topographical map
    * <u>Required</u>: <b>CreateScoreRadarOverview</b> a function that takes in a pandas dataframe as input, visualizes the subscores for a certain campus nicely in a radar chart.
    * <u>Bonus1</u>: Create a function <b>CreateScoreRadarOverviewMulti</b> that takes a pandas dataframe with the coverage of multiple campus areas and displays them in one radar view for comparison. 
    * <u>Bonus2</u>: Add an extra dimension to this challenge: Create a function <b>GetMODISdata</b> that, given a placename, derives from MODIS data the vegetation coverages for the centroid of the place. 
          * For this, the [MODIS Web Service](https://modis.ornl.gov/data/modis_webservice.html) was used.
          * Extract the average values for the layers 'Percent_Tree_Cover', 'Percent_NonTree_Vegetation', 'Percent_NonVegetated' of the MODIS product [MOD44B](https://lpdaac.usgs.gov/products/mod44bv006/).


