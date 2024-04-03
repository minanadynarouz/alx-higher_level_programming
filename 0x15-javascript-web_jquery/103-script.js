$(document).ready(function () {
    const langCode = $('input#language_code').val();
    const API_URL = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;

    $("#btn_translate").on("click keypress", (event) => {
        if ((event.type === "keypress" && event.which === 13) || event.type === "click") {
            $.get(API_URL, (res) => {
                $("#hello").text(res.hello);
            });
        }
    });
});
