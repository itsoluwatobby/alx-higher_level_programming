-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id

SELECT ts.title, tg.genre_id 
FROM tv_shows AS ts INNER JOIN tv_shows_genres AS tg
ON ts.id = tg.show_id
ORDER BY ts.title ASC, tg.genre_id ASC;
