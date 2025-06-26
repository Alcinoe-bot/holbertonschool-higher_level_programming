-- genre id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows ts, tv_show_genres tg
WHERE tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
