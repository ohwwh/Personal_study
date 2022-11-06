const h1 = document.querySelector("div.hello:first-child h1");

function colorChangeClick(){
    h1.style.color = "white";
}

function colorChangeEnter(){
    h1.style.color = "blue";
    console.log("mouse is here");
    h1.innerText = "mose is here"
}

function colorChangeLeave(){
    h1.style.color = "red";
    console.log("mouse is gone");
    h1.innerText = "mouse is gone"
}

function handleResize(){
    document.body.style.backgroundColor = "tomato";
}

function handleCopy(){
    alert("Copy is prohibited!");
}

function handleWifiOff(){
    alert("wifi is gone!");
}

h1.addEventListener("click", colorChangeClick);
h1.addEventListener("mouseenter", colorChangeEnter);
h1.addEventListener("mouseleave", colorChangeLeave);
window.addEventListener("resize", handleResize);
//h1.addEventListener("copy", handleCopy);
window.addEventListener("copy", handleCopy);
window.addEventListener("offline", handleWifiOff);