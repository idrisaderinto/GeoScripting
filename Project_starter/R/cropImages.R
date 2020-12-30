# GeoScipting 2020
# Project
# Title: 
# TEAMNAME: Fried Plantain
# NAME OF TEAM MEMBERS: Margret Azuma and Busra Bozkurt
# DATE: 24/01/2020

# Function that created a crop within a given extent area
cropImages <- function(rasterBrick, extentArea){
  
  # Create crop
  createCrop <- crop(rasterBrick, extentArea)
  
  createMask <-  mask(createCrop, extentArea)
  return(createMask)
}