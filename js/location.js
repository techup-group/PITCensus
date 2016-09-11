 function embedGoogleMap(divId) 
 {
     var location = getLocation();

     // Google-ready coordinates
     var coords = new google.maps.LatLng(location.lat, location.long);

     // set options for map (max zoom = 20)
     var mapOptions = {
         zoom: 16,
         center: coords,
         mapTypeId: google.maps.MapTypeId.ROADMAP
     }
         
     // create map with marker at coordinates
     var map = new google.maps.Map(document.getElementById(divId), mapOptions);
     var marker = new google.maps.Marker({
         map: map,
         position: coords
     });
 }
 
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

function getLocation()
{
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
}

function getLocationString()
{
	var location = getLocation();
	return location.lat + "|" + location.long;
}


