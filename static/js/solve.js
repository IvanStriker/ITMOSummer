(function() {
const curUl = document.getElementById("answers");
const lst = curUl.querySelectorAll("li");
inx = 0;
while (inx < lst.length) {
    lst[inx].querySelector("label").innerHTML = "№ " + (inx + 1).toString();
    inx += 1;
}
}());

(function () {
const items = document.querySelectorAll(".checkboxSolve");
items[0].querySelector("i").className = "fas fa-check";
for (a of items) {
    a.addEventListener('click', function(event) {
        j = event.target.closest(".checkboxSolve").querySelector("i")
        if (j.className == "") {
            j.className = "fas fa-check";
            number = j.closest("li").querySelector("label").innerHTML;
            curUl = j.closest("ul");
            curLiList = curUl.querySelectorAll("li");
            curInx = 0;
            while (curInx < curLiList.length) {
                if (curLiList[curInx].querySelector("label").innerHTML != number) {
                    curLiList[curInx].querySelector("i").className = "";
                }
                curInx += 1;
            }
        } else {
            j.className = "";
        }
    });
}
}());

(function () {
const solveButton = document.getElementById("solveButton");
solveButton.addEventListener('click', function(event) {
    form = document.getElementById("solveProblemForm");
    inputField = document.createElement("input");
    inputField.name = "problemId";
    inputField.value = document.querySelector(".problem-number strong").innerHTML.substring(2);
    form.appendChild(inputField);
    for (li of document.getElementById("answers").querySelectorAll("li")) {
        if (li.querySelector(".checkboxSolve").querySelector("i").className != "") {
            inputField = document.createElement("input");
            inputField.type = "checkbox";
            inputField.checked = true;
            inputField.name = li.querySelector("label.invisible").innerHTML;
            form.appendChild(inputField);
        }
    }
    form.submit();
});
}());
