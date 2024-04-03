$("#toggle_header").on("click", function () {
    if ($("header").hasClass("green red")) {
        $("header").toggleClass("green");
    } else if (!($("header").hasClass("red") && $("header").hasClass("green"))) {
        $("header").toggleClass("red");
    }
});