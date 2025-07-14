for (textarea of document.querySelectorAll("textarea")) {
    textarea.spellcheck=false;
}
for (input of document.querySelectorAll("input")) {
    input.autocomplete="off";
    input.spellcheck = "false";
}
