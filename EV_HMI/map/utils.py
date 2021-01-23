import json

from EV_HMI import settings
from charger.models import ChargingStation


def json_stations():
    charging_stations = {'charging_stations': []}
    for station in ChargingStation.objects.all():
        charging_points = []
        for charging_point in station.get_chargingpoints():
            charging_points.append(charging_point.id)
        charging_stations['charging_stations'].append({
            'id': station.id,
            'name': station.name,
            'lat': station.lat,
            'lng': station.lng,
            'charging_points': charging_points
        })
        if station.company:
            charging_stations['charging_stations'].append({
                'company': station.company.group.name,
            })
    try:
        with open('map/static/js/data/stations.json', 'w') as outfile:
            json.dump(charging_stations, outfile, indent=4)
    except FileNotFoundError:
        with open(settings.BASE_DIR+'/map/static/js/data/stations.json', 'w') as outfile:
            json.dump(charging_stations, outfile, indent=4)

