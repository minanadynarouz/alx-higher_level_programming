$.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    success: (res) => {
        for (let film of res.results) {
            $("#list_movies").append(`<li>${film.title}</li>`)
        }
    }
});