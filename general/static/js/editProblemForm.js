(function() {
const curUl = document.getElementById("answers");
const lst = curUl.querySelectorAll("li");
inx = 0;
while (inx < lst.length) {
    lst[inx].querySelector("label").innerHTML = "№ " + (inx + 1).toString();
    lst[inx].querySelector("input").name = "ans " + (inx + 1).toString();
    curButton = lst[inx].querySelector(".trash-button");
    curButton.addEventListener("click", function(event) {
        const curLi = event.target.closest("li");
        mylst = event.target.closest("ul");
        mylst.removeChild(curLi);
        lis = mylst.querySelectorAll("li");
        num = 1;
        while (num <= lis.length) {
            lis[num - 1].querySelector("label").innerHTML = "№ " + num.toString();
            lis[num - 1].querySelector("input").id = num.toString();
            lis[num - 1].querySelector("input").name = num.toString();
            num += 1;
        }
    });
    inx += 1;
}

}());