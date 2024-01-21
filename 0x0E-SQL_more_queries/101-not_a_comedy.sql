-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT @comedy_genre_id := id
FROM tv_genres
WHERE name = 'Comedy';

-- List all show ids without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id != @comedy_genre_id OR tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title;
