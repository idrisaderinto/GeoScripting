# Exercise 6: Vector - Raster
# Solution

## Greenest municipality

Last week end, on a rainy Saturday afternoon in Wageningen, my friend and I decided to go for a coffee. We had met at the market, while shopping for fresh vegetables, when we thought of moving to a warmer and drier place to catch up a bit since last time we had met a month ago. We were both sitting in the cafe; me by the window and he, sitting on the opposite side of the table, facing the rest of the busy room. The chattering of the crown behind me, mixed with the clinking of glasses and the hissing sound of the espresso machine releasing its vapour was giving the feeling of an old movie to the place. The rain beating the window was only adding to this atmosphere. As we were discussing, I was contemplating the rain drops rolling down the glass, on the other side of the window; gaining speed and chasing each others on the smooth surface, then being pushed out of their trajectory by a sudden burst of wind, and gaining momentum again. He suddently exclaimed:

*'Did you know that Hoenderloo is the greenest city in the Netherlands?'*

I was shocked, not only this had absolutely nothing to do with our conversation, but also I had always thought that Wageningen was the greenest city in The Netherlands. At least that's what I wanted to believe. So that I responded:

*'No way man, it can't be greener than Wageningen. Wageningen is way greener than Hoenderloo.'* Insisting on the "way" and pronouncing Hoenderloo in an english way.

*'Are you sure?'*

*'Definitely!'* I had no idea.

To what he responded, noticing my bluffing face:

*'Haha, if only we could check.'*

*''If only ...''*, these two words kept bouncing in my mind. So much that I could not follow the rest of our conversation. Whether he was talking about the influence of China on Wageningen architecture, the maximum speed of a Leopard chasing a Gazelle, his last trip to Bolivia or the true origin of the french fries name, I do not remember. I was obsessed by this thought; how could I find which was the greenest place? He did most of the talking, while my mind was trying to organize the ideas and sort preliminary hypotheses. When suddently he got my attention again:

*'Hey let's go!'*

The rain had stopped. We got up, paid our coffees to the counter, exited the cafe and each started walking in a different direction. I had almost reached the end of the street when I turned around and shouted in his direction.

*'I think we can check!'*

*'Check what?'*

I gave him a sign with my arm indicating that it didn't matter and kept walking home.


### Your task
Please help me find out which "municipality" in the Netherlands was the greenest:

- in January

- in August

- on average over the year

To measure greenness, use MODIS NDVI raster data. For the administrative boundaries you can use GADM data. Think of a nice way to visualize the results in at least one map, and save this map in an output folder.

### Data
- You can find the MODIS NDVI data [here](https://raw.githubusercontent.com/GeoScripting-WUR/VectorRaster/gh-pages/data/MODIS.zip)

- More information about MODIS can be found [here](https://lpdaac.usgs.gov/dataset_discovery/modis/modis_products_table/mod13a3_v006) 


### Requirements
- The greenest municipality in January should be stored in the variable `jan_mun`

- The greenest municipality in August should be stored in the variable `aug_mun`

- The greenest municipality on average over the year should be stored in the variable `year_mun`

- The data should be downloaded in your script to a `data` folder you create in your script: it should not be uploaded to your repository

- Similarly, the output folder and `png` file of your map should not be uploaded to your repository

- Proper Git use: both team members have to contribute to the Git repository, with a minimum of 3 commits in total



### Hints
- Use nlMunicipality <- getData('GADM',country='NLD', level=2)

### Bonus
- As a bonus task, try to find the greenest *province* in January. Store the name of the province in the variable `jan_prov`
- Hint: see `?raster::aggregate`

