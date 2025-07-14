const element = document.getElementById("settingsSaveButton");
element.addEventListener("click", function() {
    const form = document.querySelector(".personal-main-content");
    form.submit();
});