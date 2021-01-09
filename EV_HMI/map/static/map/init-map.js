let map;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        minZoom: 5,
        center: { lat: 46.7919, lng: 8.2255 },
        zoom: 8,
        scaleControl: true,
        fullscreenControl: false,
    });

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };
            if (pos.lat > 36 && pos.lat < 70 && pos.lng > -10 && pos.lng < 40) {
                map.setCenter(pos);
                map.setZoom(10)
            }
        });
    }
}
