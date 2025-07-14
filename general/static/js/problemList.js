const items = document.querySelectorAll(".checkbox");
for (a of items) {
    a.addEventListener('click', function(event) {
        j = event.target.closest(".checkbox").querySelector("i")
        if (j.className == "") {
            j.className = "fas fa-check";
        } else {
            j.className = "";
        }
    });
}
/*
const items2 = document.querySelectorAll(".trash-button");
for (a of items2) {
    a.addEventListener('click', function(event) {
        curLi = event.target.closest("li");
        curUl = event.target.closest("ul");
        curUl.removeChild(curLi);
    });
}*/

const sendButton = document.getElementById("send");
sendButton.addEventListener('click', function(event) {
    curUl = document.querySelector(".problem-ul-elems");
    collection = curUl.querySelectorAll("li");
    curInx = 0;
    res = [];
    form = document.querySelector(".invisible")
    while (curInx < collection.length) {
        formInput = document.createElement("input");
        formInput.type = "checkbox";
        formInput.name = collection[curInx].querySelector("label").innerHTML.substring(2);
        formInput.checked = (collection[curInx].querySelector(".checkbox").querySelector("i").className != "");
        form.appendChild(formInput);
        curInx += 1;
    }
    form.submit();
});