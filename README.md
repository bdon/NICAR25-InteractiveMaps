# NICAR25: Unlocking Interactive Maps for Newsrooms

* Link to this README: [bit.ly/nicar25-protomaps](https://bit.ly/nicar25-protomaps)
* Opening the developer console on mac: `Command + Option + i`
* SLIDES: [r2-public.protomaps.com/NICAR25.pdf](https://r2-public.protomaps.com/NICAR25.pdf)
* [Feedback form](https://docs.google.com/forms/d/e/1FAIpQLSfVyWnRlovof8-lXfXFXw4EbHzSrJjMuB2S1ZLA7J-JQaIEFQ/viewform?usp=dialog)

## Tools

* [Protomaps Docs](https://docs.protomaps.com)
* [MapLibre GL JS](https://github.com/maplibre/maplibre-gl-js)
* [tippecanoe](https://github.com/felt/tippecanoe)
* [pmtiles command line tool](https://github.com/protomaps/go-pmtiles)

* python3

* [PMTiles viewer (pmtiles.io)](https://pmtiles.io)
* [Placemark](https://play.placemark.io)

## Datasets

* [Open Data Minneapolis](https://opendata.minneapolismn.gov)
  * [Motorized Foot Scooter and eBike Trips 2023](https://opendata.minneapolismn.gov/datasets/cityoflakes::motorized-foot-scooter-and-ebike-trips-2023/about)
  * ["The Hennepin GIS Open Data site offers GIS data to the public free of charge and without need for a license. This site provides the ability to explore, view, share, consume, or download data."](https://gis-hennepin.hub.arcgis.com/pages/about-hennepin-gis)
* [TheUpshot/presidential-precinct-map-2020](https://github.com/TheUpshot/presidential-precinct-map-2020)
* [Protomaps Basemaps](https://docs.protomaps.com/basemaps/downloads)

## Starting a static file server

```sh
python3 -m RangeHTTPServer
```

## Tasks

* [Task 1](task1)
* [Task 2](task2)
* [Task 3](task3)

## Commands

```sh
python create_geojson.py

pmtiles show tiles/basemap_minneapolis.pmtiles

# detroit extract
pmtiles extract https://build.protomaps.com/20250306.pmtiles —-bbox=-83.1379,42.2801,-82.9600,42.3751

tippecanoe points.geojson -o points.pmtiles --force --drop-fraction-as-needed
tippecanoe lines.geojson -o lines.pmtiles --force --drop-fraction-as-needed

# more options:
# --maximum-tile-bytes=50000
# --maximum-drop-fraction-as-needed
# --maximum-zoom=7

tippecanoe precincts-with-results.geojson -o precincts.pmtiles
```

## More Info

* Last year's workshop: [eyeseast/self-hosted-maps-codespace](https://github.com/eyeseast/self-hosted-maps-codespace)
* [Daniel Wood - Cheap and Pricey: NPR Leveraged Free Tools To Build and Host Our Own Slippy Maps](https://www.youtube.com/watch?v=Abbto_9nNtc)
* [Chris Amico - How to make self-hosted maps that work everywhere and cost next to nothing](https://www.muckrock.com/news/archives/2024/feb/13/release-notes-how-to-make-self-hosted-maps-that-work-everywhere-cost-next-to-nothing-and-might-even-work-in-airplane-mode/)
* [Kevin Schaul - How The Post is replacing Mapbox with open source solutions](https://kschaul.com/post/2023/02/16/how-the-post-is-replacing-mapbox-with-open-source-solutions/)


## License

Workshop materials: [Creative Commons CC-BY](https://creativecommons.org/licenses/by/4.0/deed.en)