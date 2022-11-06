const images = ["img/0.jpeg", "img/1.jpeg"];

const chosenImage = images[Math.floor(Math.random() * images.length)];
const bgImage = document.createElement("img");
bgImage.src = chosenImage;
document.body.appendChild(bgImage);