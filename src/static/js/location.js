"use strict";

/* JavaScript to deal with Google maps and date/type embedding */

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
    function success(position) {
        callback && callback(null, position.coords);
    }

    function failure() {
        callback && callback("Failed to get position; user cancled?", null);
    }

    navigator.geolocation.getCurrentPosition(success, failure);
}

function embedGoogleMap(divId) 
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
        var map = new google.maps.Map(divId, mapOptions);
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

