-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT sh.title
FROM tv_shows AS sh
JOIN tv_show_genres AS sh_gen
	ON sh.id = sh_gen.show_id
JOIN tv_genres AS gen
	ON sh_gen.genre_id != 5
ORDER BY sh.title ASC;
