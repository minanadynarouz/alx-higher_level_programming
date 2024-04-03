$(document).ready(function () {
    $("#btn_translate").on("click", () => {
        const langCode = $('input#language_code').val();
        const API_URL = `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`;

        $.get(API_URL, (res) => {
            $("#hello").text(res.hello);
        });
    })
});