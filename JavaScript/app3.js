const h1 = document.querySelector("div.hello:first-child h1");

/*function colorChangeClick(){
    const clickedClass = "active"
    if (h1.classList.contains(clickedClass))
        h1.classList.remove(clickedClass);
    else
        h1.classList.add(clickedClass);
}*/

function colorChangeClick(){
    h1.classList.toggle("active");
}

h1.addEventListener("click", colorChangeClick);