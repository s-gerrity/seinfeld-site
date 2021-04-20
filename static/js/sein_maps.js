'use strict';

// import os from 'os';

// API_KEY = os.environ.get('API_KEY')

// start up the map
function initMap() {

    // needs fixed starting location upon load 
    const center = {lat: 37.826996, lng: -122.26186};
    const map = new google.maps.Map(document.getElementById('map'), {
      // 0 is Earth view  
      zoom: 14,
      center: center
    });
    const marker = new google.maps.Marker({
      position: center,
      map: map
    });
  }


  let locations = [
    ['Los Angeles', 34.052235, -118.243683],
    ['Santa Monica', 34.024212, -118.496475],
    ['Redondo Beach', 33.849182, -118.388405],
    ['Newport Beach', 33.628342, -117.927933],
    ['Long Beach', 33.770050, -118.193739]
  ];

const infowindow =  new google.maps.InfoWindow({});
let marker, count;
for (count = 0; count < locations.length; count++) {
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations[count][1], locations[count][2]),
      map: map,
      title: locations[count][0]
    });
google.maps.event.addListener(marker, 'click', (function (marker, count) {
      return function () {
        infowindow.setContent(locations[count][0]);
        infowindow.open(map, marker);
      }
    })(marker, count));
  }
  