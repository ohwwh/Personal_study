const clock = document.querySelector("#clock");

function getClock(){
    const date = new Date();
    //console.log(date.getHours() + " : " + date.getMinutes() + " : " + date.getSeconds());
    const hour = String(date.getHours()).padStart(2, '0');
    const minute = String(date.getMinutes()).padStart(2, '0');
    const second = String(date.getSeconds()).padStart(2, '0');
    clock.innerText = `${hour} : ${minute} : ${second}`;
}

getClock();
setInterval(getClock, 1000);