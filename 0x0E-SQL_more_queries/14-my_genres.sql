-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT gen.name
FROM tv_genres AS gen
JOIN tv_show_genres AS sh_gen
	ON gen.id = sh_gen.id
JOIN tv_shows AS sh
	ON sh.id = sh_gen.id
WHERE sh.title = 'Dexter'
ORDER BY gen.name;
