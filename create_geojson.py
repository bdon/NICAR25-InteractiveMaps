import json
import csv
import sys
import random
from datetime import datetime

random.seed(42)

# load the GeoJSON into memory, calculating midpoints

objectids = {}

with open('data/MPLS_Centerline.geojson') as g:
  j = json.loads(g.read())
  for centerline in j['features']:
    props = centerline['properties']
    coordinates = centerline['geometry']['coordinates']
    first = coordinates[0]
    last = coordinates[-1]
    objectid = int(props['GBSID'])
    objectids[objectid] = {
      'streetname':props['STREETNAME'],
      'type':props['TYPE'],
      'sufdir':props['SUFDIR'],
      'coordinates':[first,last]
    }

rows = 0
found = 0
point_features = []
line_features = []

with open('data/Motorized_Foot_Scooter_and_eBike_Trips_2023_-2732496373249609372.csv') as m:
  reader = csv.DictReader(m)
  for row in reader:
    rows = rows + 1
    start = row['StartCenterlineID']
    end = row['EndCenterlineID']
    if len(start) == 8 and len(end) == 8:
      startID = int(float(start))
      endID = int(float(end))


      if startID in objectids and endID in objectids:
        start = objectids[startID]['coordinates']
        t = random.random()
        startPoint = [start[0][0] + t * (start[1][0] - start[0][0]), start[0][1] + t * (start[1][1] - start[0][1])]

        end = objectids[endID]['coordinates']
        t = random.random()
        endPoint = [end[0][0] + t * (end[1][0] - end[0][0]), end[0][1] + t * (end[1][1] - end[0][1])]

        split = row['StartTime'].split(' ')
        date_obj = datetime.strptime(split[0], "%m/%d/%Y")
        day_category = "weekday"
        if date_obj.weekday() >= 5:
          day_category = "weekend" 

        time_category = "other"
        hour = int(split[1].split(':')[0])
        if split[2] == "PM":
          if hour < 6 or hour == 12:
            time_category = "afternoon"
          else:
            time_category = "evening"
        else:
          if hour >= 6 and hour < 12:
            time_category = "morning"

        found = found + 1
        point_features.append({
          'type':'Feature',
          'properties':{
            'point':'start',
            'vehicleType':row['vehicleType'],
            'time':row['StartTime'],
            'day_category':day_category,
            'time_category':time_category
          },
          'geometry':{
            'type':'Point',
            'coordinates':startPoint
          }
        })
        point_features.append({
          'type':'Feature',
          'properties':{
            'point':'end',
            'vehicleType':row['vehicleType'],
            'time':row['EndTime'],
            'day_category':day_category,
            'time_category':time_category
          },
          'geometry':{
            'type':'Point',
            'coordinates':endPoint
          }
        })
        line_features.append({
          'type':'Feature',
          'properties':{
            'vehicleType':row['vehicleType'],
            'startTime':row['StartTime'],
            'endTime':row['EndTime'],
            'day_category':day_category,
            'time_category':time_category
          },
          'geometry':{
            'type':'LineString',
            'coordinates':[startPoint,endPoint]
          }
        })

print("Trips in CSV:", rows)
print("Trips geolocated:", found)

with open('lines.geojson','w') as out:
  out.write(json.dumps({
    'type':'FeatureCollection',
    'features': line_features
  }))

with open('points.geojson','w') as out:
  out.write(json.dumps({
    'type':'FeatureCollection',
    'features': point_features
  }))