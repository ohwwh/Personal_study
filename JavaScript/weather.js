const API_KEY = "b2c33a3f3246aa23f697872e9b0e2600";

function GeoOk(position){
    const lat = position.coords.latitude;
    const lng = position.coords.longitude;
    console.log("You live in", lat, lng);
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${API_KEY}&units=metric`
    fetch(url)
        .then((response) => response.json())
        .then((data) => {
            const weather = document.querySelector("#weather span:first-child");
            const city = document.querySelector("#weather span:last-child");
            const temp = document.querySelector("#weather span:nth-child(2)");
            city.innerText = data.name;
            weather.innerText = data.weather[0].main;
            temp.innerText = data.main.temp
        });
}

function GeoFail(){
    alert("Can't find you!");
}

navigator.geolocation.getCurrentPosition(GeoOk, GeoFail);