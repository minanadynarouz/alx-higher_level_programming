-- List all genres not linked to the show Dexter.
SELECT gen.name
FROM tv_genres AS gen
LEFT JOIN tv_show_genres AS sh_gen
    ON gen.id = sh_gen.genre_id
LEFT JOIN tv_shows AS sh
    ON sh.id = sh_gen.show_id AND sh.title = 'Dexter'
WHERE sh.id IS NULL
ORDER BY gen.name;

