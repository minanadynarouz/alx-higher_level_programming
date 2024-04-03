$.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    success: (res) => {
        $("#hello").text(res.hello);
    }
});