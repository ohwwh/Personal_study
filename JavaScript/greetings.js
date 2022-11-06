const loginForm = document.querySelector("#LogIn");
const loginInput = loginForm.querySelector("input");
const loginButton = loginForm.querySelector("button");
const loginLink = document.querySelector("h1 a");
const greeting = document.querySelector("#greeting");


/*function ButtonClick(){
    const value = loginInput.value;
    if (value == "")
        alert("Input needed");
    else if (value.length > 15)
        alert("too long");  
}*/

function logInSubmit(event){
    event.preventDefault();
    console.log(event);
    const username = loginInput.value;
    loginForm.classList.add("hidden");
    localStorage.setItem("username", username);
    greeting.innerText = "Hello " + username;
    greeting.classList.remove("hidden");
}

//event

/*function linkClick(event){
    event.preventDefault();
}*/
//loginLink.addEventListener("click", linkClick);

const savedUserName = localStorage.getItem("username");
if (savedUserName == null){
    loginForm.classList.remove("hidden");
    loginForm.addEventListener("submit", logInSubmit);
}
else{
    greeting.classList.remove("hidden");
    greeting.innerText = "Hello " + savedUserName;
}