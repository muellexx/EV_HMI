function loadStations() {
    $.getJSON("/static/js/data/stations.json", function(json){
        stations = json.charging_stations;
        for (let i = 0; i < stations.length; i++) {
            var iStation = stations[i];
            var coordinates = new google.maps.LatLng(stations[i].lat, stations[i].lng);
            var url = "/media/icons/map/MarkerEdrop2.png";

            var image = {
                url: url,
                size: new google.maps.Size(36,48),
                anchor: new google.maps.Point(16,48)
            };

            var station = new google.maps.Marker({
                position: coordinates,
                icon: image,
                map: map
            });

            station.setMap(map);
        }
    });
}