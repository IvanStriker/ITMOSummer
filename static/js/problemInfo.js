const curUl = document.getElementById("answers");
const lst = curUl.querySelectorAll("li");
inx = 0;
while (inx < lst.length) {
    lst[inx].querySelector("label").innerHTML = "№ " + (inx + 1).toString();
    inx += 1;
}