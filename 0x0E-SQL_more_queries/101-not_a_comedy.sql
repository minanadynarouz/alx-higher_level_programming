-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT @comedy_genre_id := id
FROM tv_genres
WHERE name = 'Comedy';

SELECT sh.title
FROM tv_shows AS sh
LEFT JOIN tv_show_genres AS sh_gen
	ON sh.id = sh_gen.show_id
WHERE sh_gen.genre_id != @comedy_genre_id OR sh_gen.genre_id IS NULL
ORDER BY sh.title;
