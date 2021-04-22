'use strict';


function initMap() {
  // set center of the map to load on this location
  var mapsApiStr = "";
  var url = window.location.href;

  if (url.includes("zip-code")) {
    var zipCode = url.slice(-5);
    mapsApiStr = 'https://maps.googleapis.com/maps/api/geocode/json?address='+ zipCode +'&key=';
    
  } else {
      mapsApiStr = 'https://maps.googleapis.com/maps/api/geocode/json?address=10024&key=';
  }

  $.get(mapsApiStr, (res) => {

    var center = {lat: res.results[0].geometry.location.lat,
                lng: res.results[0].geometry.location.lng};


    // show map at id #map with zoom 10 (0 is earth view) and center at the var center
    let map = new google.maps.Map(document.getElementById('map'), {
      zoom: 12,
      center: center
    });

    
    $("#zip-button").on("click", (evt) =>{
      evt.preventDefault();

      var zip = $("#zip-code").val();

      // redirecting to new page with zip code search; same way of doing the other request w +
      // window is for referencing anything in the window / page including the url
      // location is the area you want to change
      window.location.href=`/zip-code?zip-code=${zip}`

      // $.get('https://maps.googleapis.com/maps/api/geocode/json?address='+ zip +'&key=', (res) => {

      //   var newCenter = {lat: res.results[0].geometry.location.lat,
      //                   lng: res.results[0].geometry.location.lng}; 

      //   map.setCenter(newCenter);
      // });

    });


    let locations = [
      // ['Los Angeles', 34.052235, -118.243683],
      ['Santa Monica', 34.024212, -118.496475],
      ['Redondo Beach', 33.849182, -118.388405],
      ['Newport Beach', 33.628342, -117.927933],
      ['Long Beach', 33.770050, -118.193739]
    ];

    // create a pop up window that you can click to show info 
    const infowindow = new google.maps.InfoWindow({});
    // create variables marker and count
    let marker;
    let count;
    // iterate through each location in the list of locations
    for (count = 0; count < locations.length; count++) {
      // make a marker
      marker = new google.maps.Marker({
        // extract lat and lon from the locations array
        position: new google.maps.LatLng(locations[count][1], locations[count][2]),
        // use the map var as the map
        map: map,
        // the title is the first index in the list in the array locations
        title: locations[count][0]
      });
      // when marker is clicked, create function that takes in 2 arguements 
      google.maps.event.addListener(marker, 'click', (function (marker, count) {
        // then run the function to show the pop up on the marker
        return function () {
          infowindow.setContent(locations[count][0]);
          infowindow.open(map, marker);
        }
        // passing values to the function
      })(marker, count));
    }
  });
}