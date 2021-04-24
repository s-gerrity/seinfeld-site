'use strict';


function initMap() {
  
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
    });


  $("#zip-button").on("click", (evt) =>{
    evt.preventDefault();

  });


  // // // // // MAKE MARKERS // // // // // //
  const infowindow = new google.maps.InfoWindow({});
  let marker;
  let count;

  for (count = 0; count < Object.keys(latLng).length; count++) {
    marker = new google.maps.Marker({

      position: new google.maps.LatLng(Object.values(latLng)[count][1], Object.values(latLng)[count][0]),
      map: map,
      title: Object.keys(latLng)[count]
      
    });
    
    // when marker is clicked, create function that takes in 2 arguements 
    google.maps.event.addListener(marker, 'click', (function (marker, count) {

      return function () {
        infowindow.setContent(Object.keys(latLng)[count]);
        infowindow.open(map, marker);

      }
      // passing values to the function
    })(marker, count));
  }
  });
  }