"use strict";

function getTimeString() 
{
    var current_date = new Date();
    return current_date.getHours() + ":" + current_date.getMinutes();
}

function getDateString() 
{
    var current_date = new Date();
    return current_date.getMonth() + 1 + "/" + current_date.getDate() + "/" + current_date.getFullYear();
}

function getLocation(callback) 
{
<<<<<<< HEAD
     x = navigator.geolocation;
     x.getCurrentPosition(success, failure);
     var retlat = 0;
     var retlong = 0;

     function success(position) {
         retlat = position.coords.latitude;
         retlong = position.coords.longitude;
     }

     function failure(err) {
        console.warn('ERROR(' + err.code + '): ' + err.message);
        console.log("Failed to get position; user cancled?")
     }
     
 	return { lat:retlat, long:retlong }    
=======
    function success(position) {
        callback && callback(null, position.coords);
    }

    function failure() {
        callback && callback("Failed to get position; user cancled?", null);
    }

    navigator.geolocation.getCurrentPosition(success, failure);
>>>>>>> eadd87ec5e039d0a656283eeb508651ae920abf4
}

function embedGoogleMap(div) 
{
    getLocation(function(error, location) {
        if (error) {
            console.log("Failed to embed map: " + error);
            return;
        }

        // Google-ready coordinates
        var coords = new google.maps.LatLng(location.latitude, location.longitude);

        // set options for map (max zoom = 20)
        var mapOptions = {
            zoom: 16,
            center: coords,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }

        // create map with marker at coordinates
        var map = new google.maps.Map(div, mapOptions);
        var marker = new google.maps.Marker({
            map: map,
            position: coords
        });
    });
}

function getLocationString(callback) 
{
    getLocation(function(error, location) {
        if (error) {
            callback && callback(error, null);
            return;
        }
        callback && callback(null, location.latitude + "|" + location.longitude);
    });
}
