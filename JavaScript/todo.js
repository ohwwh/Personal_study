const toDoForm = document.querySelector("#todo-form");
const toDoList = document.querySelector("#todo-list");
const toDoInput = toDoForm.querySelector("input");
let toDos = [];

/*function removeByID(item){
    if (item.id == li.id)
        return false;
    else
        return true;
}*/

function saveToDos(event){
    localStorage.setItem("todos", JSON.stringify(toDos));
    //localStorage.setItem("todos", toDos);
    //이렇게 하면...arguments. 내용이 저장이 되는게 아니라 그냥 todos에 object, object, 이런식으로 들어간다 흑흑
}

function deleteToDo(event){
    const li = event.target.parentElement;
    toDos = toDos.filter((item) => item.id != parseInt(li.id));
    // => 자스식 함수 표기법. 
    //function anything(item){return (item.id != parseInt(li.id))}의 축약버젼
    //localStorage.removeItem("todos");
    //이걸 굳이 안해줘도 setItem하면 알아서 대체가 되더라
    saveToDos();
    li.remove();
}

function paintToDo(newToDo){
    const li = document.createElement("li");
    const span = document.createElement("span");
    const button = document.createElement("button");
    li.appendChild(span);
    li.appendChild(button);
    span.innerText = newToDo.text;
    li.id = newToDo.id;
    button.innerText = "❌";
    button.addEventListener("click", deleteToDo);
    toDoList.appendChild(li);
}

function handleToDoSubmit(event){
    event.preventDefault();
    const newToDo = toDoInput.value;
    toDoInput.value="";
    const newToDoObj = {
        text:newToDo,
        id:Date.now(),
    };
    toDos.push(newToDoObj);
    paintToDo(newToDoObj)
    //console.log(toDos);
    saveToDos();
}

toDoForm.addEventListener("submit", handleToDoSubmit);


const savedToDos = localStorage.getItem("todos");
if (savedToDos != null){
    toDos = JSON.parse(savedToDos);
    console.log(toDos);
    toDos.forEach((item) => paintToDo(item));
}

