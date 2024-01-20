-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tsh.title, tvg.genre_id
FROM tv_shows AS tsh
LEFT JOIN tv_show_genres AS tvg
	ON tsh.id = tvg.show_id
WHERE tvg.genre_id IS NULL
ORDER BY tsh.title, tvg.genre_id;
