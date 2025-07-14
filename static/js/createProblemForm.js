(function () {
const element = document.getElementById("createProblemButton");
element.addEventListener("click", function() {
    const form = document.getElementById("createProblemForm");
    form.submit();
});

const element2 = document.getElementById("addAnswerButton");
element2.addEventListener("click", function() {
    const lst = document.getElementById("answers");
    const newItem = document.createElement('li');
    newItem.className = "problem-form-elem";
    newItem.innerHTML = "<label>№ " + (lst.querySelectorAll("li").length + 1).toString() + "</label><input class='input' style='margin-right: 20px' id='" + (lst.childNodes.length).toString() + "'  name='ans" + (lst.childNodes.length).toString() + "'/><a class='trash-button'><i class='fas fa-minus'></i></a>";
    const i = newItem.querySelector(".trash-button");
    i.addEventListener("click", function(event) {
        const curLi = event.target.closest("li");
        lst2 = document.getElementById("answers");
        lst2.removeChild(curLi);
        lis = lst2.querySelectorAll("li");
        num = 1;
        while (num <= lis.length) {
            lis[num - 1].querySelector("label").innerHTML = "№ " + num.toString();
            lis[num - 1].querySelector("input").id = num.toString();
            lis[num - 1].querySelector("input").name = num.toString();
            num += 1;
        }
    });
    lst.appendChild(newItem);
});
}());