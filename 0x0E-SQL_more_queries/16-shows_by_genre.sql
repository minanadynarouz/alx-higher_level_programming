-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT sh.title, gen.name
FROM tv_shows AS sh
LEFT JOIN tv_show_genres AS sh_gen
	ON sh.id = sh_gen.show_id
LEFT JOIN tv_genres AS gen
	ON gen.id = sh_gen.genre_id
ORDER BY sh.title, gen.name;
