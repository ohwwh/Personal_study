const h1 = document.querySelector("div.hello:first-child h1");

function colorChangeClick(){
    const currentColor = h1.stlye.color;
    console.log(h1.style.color);
    if (h1.style.color == "blue")
        h1.style.color = "tomato";
    else
        h1.style.color = "blue";
}

h1.addEventListener("click", colorChangeClick);