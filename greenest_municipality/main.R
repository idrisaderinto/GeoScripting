# Import packages
library(raster)
library(rgdal)
library(rgeos)

# Create directories
if (!dir.exists('data')){
  dir.create('data', showWarnings = FALSE)
}

if (!dir.exists('output')){
  dir.create('output', showWarnings = FALSE)
}

# Download and unzip MODIS data in the 'data' folder
download.file(url = 'https://raw.githubusercontent.com/GeoScripting-WUR/VectorRaster/gh-pages/data/MODIS.zip', destfile = 'data/ModisNDVI', method = 'auto')
unzip('data/ModisNDVI', exdir = 'data')

# Select raster files in MODIS data and save as RasterBrick
MODISfiles = list.files(path = 'data/', pattern = glob2rx('*.grd'), full.names = TRUE)
MODISdata = brick(MODISfiles)

# Download the municipality map of the Netherlands
nlMunicipality = getData('GADM', country='NLD', level=2, path = 'data/')

# Transform GADM data to CRS of MODIS data
nlMunicipality = spTransform(nlMunicipality, crs(proj4string(MODISdata)))

# Extract the mean NDVI value of each municipality
MODISmun = extract(MODISdata, nlMunicipality, fun = mean, na.rm = TRUE)

# Calculate the greenest municipality for January
jan_mun = nlMunicipality@data$NAME_2[which.max(MODISmun[,1])]

paste(jan_mun, "was the greenest municipality in January")

# Calculate the greenest municipality for August
aug_mun = nlMunicipality@data$NAME_2[which.max(MODISmun[,8])]

paste(aug_mun, "was the greenest municipality in August")

# Calculate the greenest municipality for the whole year
year_mun = nlMunicipality@data$NAME_2[which.max(rowMeans(MODISmun))]

paste(year_mun, "was the greenest municipality of the year")

# Bonus: calculate greenest province for January
# Aggregate municipality data to provincial level 
nlProvince <- raster::aggregate(x = nlMunicipality, by = "NAME_1")

# Extract NDVI data for each province
MODISprov <- extract(MODISdata, nlProvince, fun = mean, df = TRUE)

# Select the greenest province in January
jan_prov <- nlProvince@data$NAME_1[which.max(MODISprov[,2])]

paste(jan_prov, "was the greenest province in January")


# Plot all of the results
png(filename = './output/greenest_municipalities.png')
plot(nlMunicipality, main = "Greenest places of the Netherlands", lwd = 0.3, bg = 'grey85')
plot(nlMunicipality[which.max(MODISmun[,1]), 1], add = TRUE, col = "blue")
plot(nlMunicipality[which.max(MODISmun[,8]), 1], add = TRUE, col = "yellow")
plot(nlMunicipality[which.max(rowMeans(MODISmun)), 1], add = TRUE, col = "green")
plot(nlProvince[which.max(MODISprov[,2]), 1], add = TRUE, col = "red")
legend('bottomright', c(paste0(jan_mun, ": greenest municipality in January"), paste0(aug_mun, ": greenest municipality in August"), paste0(year_mun, ": greenest municipality year round"), paste0(jan_prov, ": greenest province in January")), fill = c('blue', 'yellow', 'green', 'red'), cex = 0.70)
mtext(adj = 0, side = 1, line = -1, "Data sources: MODISnl, GADM.", cex = 0.6, col = "grey20")
dev.off()

