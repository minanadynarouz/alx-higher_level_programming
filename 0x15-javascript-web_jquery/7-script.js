$.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    success: (res) => {
        console.log(res["name"]); // undefined
    }
});

