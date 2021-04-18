'use strict';

import os from 'os';

API_KEY = os.environ.get('API_KEY')

// start up the map
function initMap() {

    // needs fixed starting location upon load 
    const center = {lat: 41.8781, lng: -87.6298};
    const map = new google.maps.Map(document.getElementById('map'), {
      // 0 is Earth view  
      zoom: 10,
      center: center
    });
    const marker = new google.maps.Marker({
      position: center,
      map: map
    });
  }
  