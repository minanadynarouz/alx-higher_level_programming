-- ist all genres not linked to the show Dexter.
SELECT gen.name
FROM tv_genres AS gen
JOIN tv_show_genres AS sh_gen
	ON gen.id = sh_gen.genre_id
JOIN tv_shows AS sh
	ON sh.id NOT = sh_gen.genre_id
WHERE sh.title = 'Dexter'
ORDER BY gen.name;
