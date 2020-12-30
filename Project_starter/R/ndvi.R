# Geoscripting 2020 
# Project 
# Title:
# TEAMNAME: Fried Plantain
# NAME OF TEAM MEMBERS: Margret Azuma and Busra Bozkurt
# DATE: 24/01/2020

## this function calculate the Normalized Differential Vegetation Index (NDVI) is a standardized vegetation index which calculated using NearInfra-red and Red bands.
#                     NDVI = (NIR – RED) / (NIR + RED)
# Where:
# RED= DN values from the RED band
# NIR= DN values from Near-Infrared band
# * NIR: Near-Infra-red Band
# * RED: Red band 

ndvi <- function(NIR, RED){
  
  # calculate NDVI 
  calNDVI <- (NIR - RED) / (NIR + RED)
  
  #return NDVI
  return(calNDVI)
}